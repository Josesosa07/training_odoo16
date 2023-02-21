# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstatePropertyTag(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------
    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    name = fields.Char(required=True)
    color = fields.Integer("Color Index")
