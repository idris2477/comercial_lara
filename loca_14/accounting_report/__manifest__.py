# -*- coding: utf-8 -*-
{
    'name': "accounting_report_lara",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account', 'website', 'account_accountant', 'sale_management', 'sales_order_vendedor'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/account_report.xml',
        'report/account_report_factura_cliente_view.xml',
        'report/account_report_notas_entrega_views.xml',
        'report/account_report_notas_debito_views.xml',
        'report/account_report_notas_credito_views.xml',
        'views/views.xml',
        #'report/views.xml',

    ],
    # only loaded in demonstration mode

}
