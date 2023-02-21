# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstatePropertyType(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------
    _name = "estate.property.type"
    _description = "Real Estate Property Type"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    name = fields.Char(required=True)
