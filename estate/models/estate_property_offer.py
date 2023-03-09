# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta

_status = [("accepted", "Accepted"), ("refused", "Refused")]


class EstatePropertyOffer(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"
    _order = "price desc"
    _sql_constraints = [
        ("check_offer_price", "CHECK(price > -0)", "The price must be strictly positive"),
    ]

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    price = fields.Float()
    state = fields.Selection(selection=_status, copy=False, string="Status")
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    property_type_id = fields.Many2one("estate.property.type", related="property_id.property_type_id", store=True)
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

    def action_accept(self):
        for record in self:
            property_record = record.property_id
            if property_record.state == "offer_accepted":
                raise UserError(_("An offer has already been accepted."))
            record.state = "accepted"
            property_record.state = "offer_accepted"
            property_record.selling_price = record.price
            property_record.buyer_id = record.partner_id
        return True

    def action_refuse(self):
        return self.write(
            {
                "state": "refused",
            }
        )

    # Lifecycle:
    @api.model
    def create(self, vals):
        if vals.get("property_id") and vals.get("price"):
            property_obj = self.env["estate.property"].browse(vals["property_id"])
            if property_obj.offer_ids:
                if fields.float_compare(vals["price"], property_obj.best_price, precision_rounding=0.01) < 0:
                    message = _("The offer must be higher than {name}").format(name=property_obj.best_price)
                    raise UserError(message)
            property_obj.state = "offer_received"
        return super().create(vals)
