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
from odoo import api, models


class EventMailRegistration(models.Model):
    _inherit = 'event.mail.registration'

    @api.multi
    def execute(self):
        """ Override parent method
        The custom behaviour will take in account only if 'filter_id' defined
            on 'event.mail' is set.
        Otherwise, will take default behaviour
        """
        for rec in self:
            if not rec.scheduler_id.filter_id:
                super(EventMailRegistration, rec).execute()

            # The domain defined in the filter selected are expected to filter
            # only registration state.
            domain = rec.scheduler_id.filter_get_domain()
            in_domain = rec.registration_id.id in domain
            if domain and in_domain and not rec.mail_sent:
                rec.scheduler_id.template_id.send_mail(rec.registration_id.id)
                rec.write({'mail_sent': True})
