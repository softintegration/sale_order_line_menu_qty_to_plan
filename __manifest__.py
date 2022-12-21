# -*- coding: utf-8 -*-

{
    'name': 'Sale order line menu with remaining to plan field',
    'version': '1.0.1.1',
    'author':'Soft-integration',
    'category': 'Sale',
    'description': "",
    'depends': [
        'sale_order_line_menu','sale_mrp_production_request'
    ],
    'data': [
        'views/sale_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
