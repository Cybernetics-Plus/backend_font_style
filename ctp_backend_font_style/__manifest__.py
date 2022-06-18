# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybernetics Plus Co., Ltd.
#    Customize Web Backend Font Style
#
###################################################################################

{
    "name": "Backend Font Style",
    'version': '15.0.1.0.1',
    'summary': """ 
            Customize Web Backend Font Style
            .""",
    'description': """ 
            Customize Web Backend Font Style
            .""",
    'author': 'Cybernetics Plus Co., Ltd.',
    'website': 'https://www.cybernetics.plus',
    'live_test_url': 'https://www.cybernetics.plus',
    'images': ['static/description/banner.png'],
    'category': 'Tools',
    "license": 'Other proprietary',
    'price': 15.00,
    'currency': 'US',
    'installable': True,
    'application': True,
    'auto_install': False,
    'contributors': [
        'Developer <dev@cybernetics.plus>',
    ],
    'depends': ['base'],
    'data': [
        'data/res_config.xml',
        'views/res_config.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'ctp_backend_font_style/static/src/js/backend_font_style.js',
            'ctp_backend_font_style/static/src/css/backend_font_style.css',
        ],
    },
}
