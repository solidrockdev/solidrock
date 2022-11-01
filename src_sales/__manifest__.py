# -*- coding: utf-8 -*-
{
    'name': "src_sales",

    'summary': """
        Sales modifications""",

    'description': """
        Sales modifications
    """,

    'author': "Ontash Pvt Ltd",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'wizard/customer_report_view.xml',
        # 'report/customer_report.xml',
        # 'report/customer_report_layout.xml',
        'report/section_quote_report_external_layout.xml',
        'report/section_quotation_report.xml',
        # 'views/menu.xml',
        'views/sale_order_inherited.xml',

    ],
    # only loaded in demonstration mode
    'application': True,
}
