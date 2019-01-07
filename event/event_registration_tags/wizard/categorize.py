# -*- coding: utf-8 -*-
# ############################################################################
#
#    Copyright Eezee-It (C) 2016
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

from odoo import api, fields, models


class EventRegistrationCategorizeWizard(models.TransientModel):

    _name = 'event.registration.categorize'
    _description = 'Categorize'

    category_ids = fields.Many2many('event.registration.category',
                                    string='Tags')

    should_reset_status_to_confirm = fields.Boolean(
        string="Reset status to confirm")

    @api.multi
    def action_apply(self):
        self.ensure_one()
        event_registration_env = self.env['event.registration'].sudo()
        active_ids = self.env.context.get('active_ids', [])
        event_registration_ids = event_registration_env.browse(active_ids)

        values = {}
        if self.category_ids:
            categories_to_add = []
            for category_id in self.category_ids.ids:
                categories_to_add.append((4, category_id, False))

            if categories_to_add:
                event_registration_ids.write({})
                values['category_ids'] = categories_to_add

        if self.should_reset_status_to_confirm:
            values['state'] = 'open'

        event_registration_ids.write(values)
        return {'type': 'ir.actions.act_window_close'}
