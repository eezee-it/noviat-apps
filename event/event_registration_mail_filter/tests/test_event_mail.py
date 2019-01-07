# -*- coding: utf-8 -*-
# #############################################################################
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
###############################################################################
from odoo.tests import TransactionCase

FILTER = 'event_registration_mail_filter.filter_event_registration_confirmed'
FILTER2 = 'event_registration_mail_filter.filter_event_registration_draft'


class TestEventMail(TransactionCase):
    def setUp(self):
        super(TestEventMail, self).setUp()
        self.event_1 = self.env.ref('event.reg_1_1')
        mail_obj = self.env['event.mail']
        self.mail_id = mail_obj.create({
            'event_id': self.env.ref('event.event_1').id,
            'interval_unit': 'days',
            'interval_type': 'after_sub',
            'template_id': self.env.ref('mail.email_template_partner').id
        })
        self.mail_id2 = mail_obj.create({
            'event_id': self.env.ref('event.event_0').id,
            'interval_unit': 'days',
            'interval_type': 'after_event',
            'template_id': self.env.ref('mail.email_template_partner').id
        })
        registration_obj = self.env['event.mail.registration']
        self.registration_id = registration_obj.create({
            'scheduler_id': self.mail_id.id,
            'registration_id': self.event_1.id,
            'mail_sent': False,
        })
        self.registration_id2 = registration_obj.create({
            'scheduler_id': self.mail_id.id,
            'registration_id': self.event_1.id,
            'mail_sent': False,
        })

    def test_all_event_in_mail(self):
        """
        Check if the number of registration in email
        is equal with number of registraion in event
        """
        self.mail_id.write({
            'filter_id': self.env.ref(FILTER).id
        })
        self.mail_id.execute()
        reg_ids = self.mail_id.mail_registration_ids.mapped('registration_id')
        event_reg_ids = self.mail_id.event_id.registration_ids
        self.assertEqual(len(reg_ids), len(event_reg_ids),
                         'Event from registration are not included')

    def test_mail_sent_status(self):
        """
        Check if email is not sent if filter is not defined or interval type
        is not after_sub
        """
        self.assertFalse(self.mail_id.filter_get_domain(),
                         'Domain should be empty since filter is not defined')
        self.registration_id.execute()
        self.mail_id.execute()
        self.assertFalse(
            self.mail_id.mail_sent,
            'Abnormality in default behaviour,'
            ' no email should be sent at this point')
        self.mail_id.write({
            'filter_id': self.env.ref(FILTER).id
        })
        self.mail_id.execute()
        self.assertFalse(self.mail_id.mail_sent,
                         'Email should not be sent immediately')
        self.registration_id2.execute()
        self.mail_id2.write({
            'filter_id': self.env.ref(FILTER).id,
            'mail_sent': False
        })
        self.mail_id2.execute()
        self.assertTrue(self.mail_id2.mail_sent,
                        'Email is expected to be sent when filter is defined')
        self.mail_id2.write({
            'filter_id': self.env.ref(FILTER2).id,
            'mail_sent': False
        })
        self.mail_id2.execute()
        self.assertTrue(self.mail_id2.mail_sent,
                        'Email is expected to be sent when filter is defined')
