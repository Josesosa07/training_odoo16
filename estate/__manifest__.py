# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    "name": "Real Estate",
    "author": "Vauxoo",
    "version": "16.0.1.0.0",
    "category": "Real Estate/Brokerage",
    "sequence": 15,
    "summary": "Track leads and close opportunities",
    "website": "https://www.odoo.com/page/realestate",
    "depends": [
        "base",
        "web",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/estate_property_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_offer_views.xml",
        "views/res_users_views.xml",
        "views/estate_menus.xml",
        "data/estate.property.type.csv",
    ],
    "demo": [
        "demo/estate_property.xml",
        "demo/estate_offer.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
