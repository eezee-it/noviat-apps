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
from odoo import api, models, _


class EventEvent(models.Model):
    _inherit = 'event.event'

    @api.multi
    def _get_registration_partner_ids(self):
        return set([r.partner_id for r in self.registration_ids])

    @api.multi
    def action_set_new_registration(self, contacts):
        """  """
        reg_obj = self.env['event.registration']
        res = {'message_notification': _('No partners have been selected')}
        if contacts:
            already_exist_contact = 0
            for contact in contacts:
                if contact not in self._get_registration_partner_ids():
                    vals = {
                        'event_id': self.id,
                        'partner_id': contact.id
                    }
                    registration = reg_obj.create(vals)
                    registration._onchange_partner()
                else:
                    already_exist_contact = already_exist_contact + 1
            message_notification = _("Following this action:\n"
                                     "* %s registrations have been added.\n"
                                     "* %s customers are already"
                                     " registered before this action.") % (
                (len(contacts) - already_exist_contact),
                                         already_exist_contact
            )

            res['message_notification'] = message_notification
        return res
