# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Real Estate",
    "author": "Vauxoo",
    "version": "16.0.1.0.0",
    "category": "Category",
    "sequence": 15,
    "summary": "Track leads and close opportunities",
    "website": "https://www.odoo.com/page/realestate",
    "depends": [
        "base",
        # 'base_setup',
        # 'sales_team',
        # 'mail',
        # 'calendar',
        # 'resource',
        # 'fetchmail',
        # 'utm',
        # 'web_tour',
        # 'contacts',
        # 'digest',
        # 'phone_validation',
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_offer_views.xml",
        "views/estate_menus.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
