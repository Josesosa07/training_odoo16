# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from dateutil.relativedelta import relativedelta

_status = [("accepted", "Accepted"), ("refused", "Refused")]


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
    validity = fields.Integer(string="Validity (days)", default=7)

    # Computed
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    # Computed methods
    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.date_deadline = date + relativedelta(days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.validity = (offer.date_deadline - date).days
