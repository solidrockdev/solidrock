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
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'report/section_quote_report_external_layout.xml',
        'report/section_quotation_report.xml',

        'views/sale_order_inherited.xml',

    ],
    # only loaded in demonstration mode
    'application':True,
}
