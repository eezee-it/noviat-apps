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

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_event_registration_tags = fields.Boolean(
        "Attendee tags")

    module_event_mass_registration = fields.Boolean(
        "Mass registration")

    module_event_registration_mail_filter = fields.Boolean(
        "Advanced Email Schedule Filters")

    module_website_multi_event = fields.Boolean(
        "Multi Events")

    module_website_event_deadline = fields.Boolean(
        "Registration deadline")

    module_website_event_images = fields.Boolean(
        "Images")

    module_website_event_public_confirmation = fields.Boolean(
        "Public confirmation")

    module_website_event_registration_code = fields.Boolean(
        "Registration code")

    module_website_event_programs = fields.Boolean(
        "Programs")

    module_website_event_list_publication = fields.Boolean(
        "Event Publication")

    module_event_registration_note = fields.Boolean(
        "Internal note")

    module_website_event_create_contact = fields.Boolean(
        "Create a contact from the registration")

    module_website_event_details = fields.Boolean(
        "Extra Informations for website event")

    module_website_event_email_details = fields.Boolean(
        "Extra Information : Content E-mails")
