# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright Eezee-It
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'VAT Report Eezee-it',
    'version': '0.1',
    'license': 'AGPL-3',
    'author': 'Eezee-It',
    'category': 'Account',
    'description': "New report for VAT declaration",
    'depends': ['base',
                'account_accountant',
                'l10n_be',
                'account_tax_code',
                'account_tax_constraints',
                'l10n_be_reports',
                'account_reports'],
    'data': ['views/account_tag_view.xml',
             'views/account_tax_view.xml',
             'data/tags_tax.xml',
             'data/tax.xml',
             'data/financial_report.xml',
             'data/financial_line_report.xml',
             'data/ir_filter.xml'],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'pre_init_hook': '_migrate_tags',
}
