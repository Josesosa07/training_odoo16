# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    "name": "Real Estate",
    "version": "1.2",
    "category": "Category",
    "sequence": 15,
    "summary": "Track leads and close opportunities",
    "description": "",
    "website": "https://www.odoo.com/page/realestate",
    "depends": [
        "base",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_menus.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
