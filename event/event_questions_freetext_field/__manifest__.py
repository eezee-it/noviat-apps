# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright Eezee-It (C) 2017
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
{
    'name': 'Free Question type on Events',
    'version': '11.0.1.0.0',
    'author': 'Eezee-It',
    'category': 'Customer Modules',
    # 'description': 'Add free question type on event questions',
    'depends': [
        'website_event_questions',
    ],
    'license': 'LGPL-3',
    'data': [
        'views/event_question.xml',
        'views/event_registration.xml',
        'views/event_answer_freetext.xml',
        'templates/event_question.xml',
        'security/ir.model.access.csv',
    ],
}
