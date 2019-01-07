# -*- coding: utf-8 -*-
# ############################################################################
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
    'name': 'Dynamic Column Listview Stock',
    'version': '11.0.1',
    'author': 'Eezee-It',
    'category': 'Web',
    'website': 'http://www.eezee-it.com',
    'summary': 'Dynamic Column Listview Stock',
    'description': """

Dynamic Column Listview Stock
============
In Odoo v11, they change field product_qty to product_uom_qty in stock move
and stock move line. If you try to fill this fields, you have an error.
This fields are filled due to the module Column List view that return all
fields. To avoid this error, we develop this module
    """,
    'depends': [
        'dynamic_column_listview',
        'stock',
    ],
    'auto_install': True,
    'data': [],
}
