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
from odoo import models, fields


class EventAnswerFreeText(models.Model):
    _name = 'event.answer.freetext'
    _order = 'sequence,id'

    name = fields.Char('Value', required=True, translate=True)
    question_id = fields.Many2one(
        'event.question', string="Question", required=True, ondelete='cascade')

    event_registration_id = fields.Many2one('event.registration',
                                            string="Attendee", required=True,
                                            ondelete='cascade')

    sequence = fields.Integer(default=10)
