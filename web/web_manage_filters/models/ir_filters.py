# -*- coding: utf-8 -*-
# ############################################################################
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
from odoo import models, api


class IrFilters(models.Model):
    _inherit = 'ir.filters'

    @api.model
    def default_get(self, fields):
        res = super(IrFilters, self).default_get(fields)
        if not res.get('model_id'):
            res['model_id'] = 'res.partner'
            res['domain'] = []
        return res

    @api.onchange('model_id')
    def _onchange_model_id(self):
        if self.model_id:
            return {'value': {'domain': []},
                    'options': {'domain': {"'model':'"+self.model_id+"'"}}}
