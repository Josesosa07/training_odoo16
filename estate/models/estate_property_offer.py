# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

_status = [
    ("accepted", "Accepted"),
    ("refused", "Refused")
]


class EstatePropertyOffer(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    price = fields.Float()
    state = fields.Selection(selection=_status, copy=False, string="Status")
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
