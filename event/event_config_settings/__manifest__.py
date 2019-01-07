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
{
    'name': 'Event Settings',
    'version': '11.0.1.0.0',
    'author': 'Eezee-It',
    'category': 'Event',
    # 'description': 'Add tags',
    'license': 'LGPL-3',
    'depends': [
        'event',
        'web_config_settings',
    ],
    'data': [
        'views/res_config_settings_views.xml'
    ],
    'auto_install': True
}
