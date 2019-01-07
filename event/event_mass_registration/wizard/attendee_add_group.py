# -*- encoding: utf-8 -*-
##############################################################################
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
##############################################################################

from odoo import fields, models, api, _
from odoo.tools.safe_eval import safe_eval

ATTENDEE_BUSINESS_MODELS = [
    'res.partner',
]


class attendee_add_group(models.TransientModel):
    _name = 'attendee.add.group'

    attendee_domain = fields.Char(
        string='Domain', oldname='domain', default=[])
    message_notification = fields.Text(
        string='Message Notification')
    mailing_model_id = fields.Many2one('ir.model', string='Recipients Model',
                                       domain=[('model',
                                                'in',
                                                ATTENDEE_BUSINESS_MODELS)])
    mailing_model_name = fields.Char(related='mailing_model_id.model',
                                     string='Recipients Model Name')

    @api.multi
    def action_select_attendee(self):
        self.ensure_one()
        view_id = self.env.ref('base.view_partner_tree', False)
        return {
            'name': _('Partners'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'tree',
            'res_model': 'res.partner',
            'views': [(view_id.id, 'tree')],
            'view_id': view_id.id,
            'target': 'new',
            'context': {},
        }

    @api.multi
    def action_add_mass_pre_registration(self):
        event_obj = self.env['event.event']
        event = event_obj.browse(
            self.env.context.get('active_id'))
        view = self.env.ref(
            'event_mass_registration.attendee_add_group_result_view_form')
        if event and self.attendee_domain:
            domain = safe_eval(self.attendee_domain)
            contacts = self.env['res.partner'].search(domain)
            res = event.action_set_new_registration(contacts)
            self.message_notification = res['message_notification']

        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'attendee.add.group',
            'target': 'new',
            'res_id': self.id,
            'views': [(view.id, 'form')],
            'type': 'ir.actions.act_window',
        }
