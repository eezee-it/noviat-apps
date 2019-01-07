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

from odoo import api, models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    email_queue_limit = fields.Integer(string="Limit")

    @api.model
    def get_values(self):

        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()

        res.update(
            email_queue_limit=int(params.get_param(
                'web_email_queue_limit.email_queue_limit', default=10000)),
        )
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()

        ir_config_parameters_env = self.env['ir.config_parameter'].sudo()
        ir_config_parameters_env.set_param(
            'web_email_queue_limit.email_queue_limit', self.email_queue_limit)
