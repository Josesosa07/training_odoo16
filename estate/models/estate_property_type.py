# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstatePropertyType(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------
    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _order = "sequence, name"  # asc or desc, by default asc
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    name = fields.Char(required=True)
    sequence = fields.Integer(default=1, help="To order stages. Lower is better.")

    # Relational (for inline view)
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")
