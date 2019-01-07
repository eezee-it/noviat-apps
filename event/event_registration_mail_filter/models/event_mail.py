# -*- coding: utf-8 -*-
# #############################################################################
#
#    Copyright Eezee-It (C) 2018
#    Author: Eezee-It <info@eezee-it.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from datetime import datetime
from odoo import api, fields, models, tools


class EventMail(models.Model):
    _inherit = 'event.mail'

    filter_id = fields.Many2one('ir.filters', string='Filter', domain=[
                                ('model_id', '=', 'event.registration')])

    @api.multi
    def filter_get_domain(self):
        """ Get domain defined in the filter
        Note: the domain are expected to filter only registration's state
        """
        self.ensure_one()
        if self.filter_id:
            domain = self.filter_id._get_eval_domain()
            model_filter = self.filter_id.model_id
            model_obj = self.env[model_filter]
            return model_obj.search(domain).ids

        return []

    @api.multi
    def execute(self):
        """ Override parent method
        Expected to send the mail only to data/records that matched
            the filter (if any)
        otherwise, will take default behaviour
        """
        for rec in self:
            if not rec.filter_id:
                super(EventMail, rec).execute()

            if rec.interval_type == 'after_sub':
                # update registration lines
                lines = []
                reg_ids = rec.mail_registration_ids.mapped('registration_id')
                for registration in rec.event_id.registration_ids.filtered(
                        lambda r: r.id not in reg_ids.ids):
                    lines.append((0, 0, {'registration_id': registration.id}))
                if lines:
                    rec.write({'mail_registration_ids': lines})
                # execute scheduler on registrations
                rec.mail_registration_ids.filtered(
                    lambda reg: reg.scheduled_date and
                    reg.scheduled_date <= datetime.strftime(
                        fields.datetime.now(),
                        tools.DEFAULT_SERVER_DATETIME_FORMAT)).execute()
            else:
                domain = rec.filter_get_domain()
                if not rec.mail_sent:
                    if domain:
                        rec.event_id.mail_attendees(
                            template_id=rec.template_id.id,
                            filter_func=lambda reg: reg.id in domain)
                        rec.write({'mail_sent': True})
                    else:
                        rec.event_id.mail_attendees(rec.template_id.id)
                        rec.write({'mail_sent': True})
