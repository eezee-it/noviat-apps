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
import threading
import datetime
import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class MailMail(models.Model):
    _inherit = "mail.mail"

    @api.model
    def process_email_queue(self, ids=None, limit=False):
        """ Override the entire Odoo method

        Send immediately queued messages, committing after each
           message is sent - this is not transactional and should
           not be called during another transaction!

           :param list ids: optional list of emails ids to send. If passed
                            no search is performed, and these ids are used
                            instead.
           :param dict context: if a 'filters' key is present in context,
                                this value will be used as an additional
                                filter to further restrict the outgoing
                                messages to send (by default all 'outgoing'
                                messages are sent).
        """
        params = self.env['ir.config_parameter'].sudo()
        limit = int(params.get_param(
            'web_email_queue_limit.email_queue_limit', default=10000))

        if not limit:
            limit = 10000

        filters = ['&',
                   ('state', '=', 'outgoing'),
                   '|',
                   ('scheduled_date', '<', datetime.datetime.now()),
                   ('scheduled_date', '=', False)]
        if 'filters' in self._context:
            filters.extend(self._context['filters'])

        filtered_ids = self.search(filters, limit=limit).ids
        if not ids:
            ids = filtered_ids
        else:
            ids = list(set(filtered_ids) & set(ids))
        res = None
        try:
            # auto-commit except in testing mode
            auto_commit = not getattr(
                threading.currentThread(), 'testing', False)
            res = self.browse(ids).send(auto_commit=auto_commit)
        except Exception:
            _logger.exception("Failed processing mail queue")
        return res
