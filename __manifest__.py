# -*- coding: utf-8 -*-
{
    'name': "Rebound Technology Website",

    'summary': "Rebound Technology Website and News management",

    'description': """
Long description of module's purpose
    """,

    'author': "Rebound Technologies",
    'website': "https://www.rebound-tech.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '17.0.1.0.4',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/footer.xml',
        'data/rebound_home.xml',
        'data/technology.xml',
        'data/sustainability.xml',
        'data/team.xml',
        'data/news.xml',
        'data/contact_us.xml',
        'data/sub_news.xml',
        'views/rebound_news_form.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'license': 'LGPL-3'
}

