# -*- coding: utf-8 -*-
# ############################################################################
#
#    Copyright Eezee-It (C) 2019
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
from odoo import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('sale_order_template_id')
    def onchange_sale_order_template_id(self):
        res = super(SaleOrder, self).onchange_sale_order_template_id()
        if not self.sale_order_template_id:
            return

        template = self.sale_order_template_id.with_context(
            lang=self.partner_id.lang)

        for template_line in \
                template.sale_order_template_line_ids.filtered('event_ok'):
            order_lines = self.order_line.filtered(
                    lambda r: r.product_id == template_line.product_id)

            for order_line in order_lines:
                if template_line.event_id.id:
                    order_line.event_id = template_line.event_id.id

                if template_line.event_ticket_id.id:
                    order_line.event_ticket_id = \
                        template_line.event_ticket_id.id
                    order_line._onchange_event_ticket_id()

        return res
