# -*- coding: utf-8 -*-
# Copyright 2018 Piotr Cierkosz (https://www.cier.tech)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name' : "Force Invoice Number",
    'version' : "12.0.1.0",
    'images': ['images/thumbnail.png'],
    'author' : "Piotr Cierkosz, Odoo Community Association (OCA)",
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'depends' : ['account'],
    'installable' : True,
    'description' : "Allows to force the Invoice Number",
    'website': "https://www.cier.tech",
    'summary': 'Allows to force the Invoice Number',
    'data': [
    'views/account_invoice_force_number_customer.xml',
    'views/account_invoice_force_number_vendor.xml',
    ],
    'live_test_url': 'https://www.youtube.com/watch?v=Rx7b3D5dRu8',
}
