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
from odoo import models, fields


class EventCategory(models.Model):
    _description = 'Attendees Tags'
    _name = 'event.registration.category'
    _order = 'parent_left, name'
    _parent_store = True
    _parent_order = 'name'

    name = fields.Char(string='Tag Name', required=True, translate=True)
    color = fields.Integer(string='Color Index')
    parent_id = fields.Many2one('event.registration.category',
                                string='Parent Category',
                                index=True, ondelete='cascade')
    child_ids = fields.One2many('event.registration.category',
                                'parent_id', string='Child Tags')
    active = fields.Boolean(default=True,
                            help="The active field allows \
                            you to hide the category without removing it.")
    parent_left = fields.Integer(string='Left parent', index=True)
    parent_right = fields.Integer(string='Right parent', index=True)
