# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from dateutil.relativedelta import relativedelta
import pytz

# Available values for the garden_orientation field.
_garden_orientation_list = [("N", "North"), ("S", "South"), ("E", "East"), ("W", "West")]
_state_list = [
    ("new", "New"),
    ("offer_received", "Offer Received"),
    ("offer_accepted", "Offer Accepted"),
    ("sold", "Sold"),
    ("canceled", "Canceled"),
]
local_timezone = pytz.timezone("America/Monterrey")


class EstateProperty(models.Model):
    # --------------------------------------- Private Attributes ----------------------------------

    _name = "estate.property"
    _description = "Real Estate Property"

    # --------------------------------------- Fields Declaration ----------------------------------
    # name = fields.Char('Estate Property Name', required=True, translate=True)
    name = fields.Char("Title", required=True, default="Unknown")
    description = fields.Text()
    postcode = fields.Char("Post Code")
    date_availability = fields.Date(
        "Available From",
        default=lambda self: (fields.Date.today() + relativedelta(months=+3)),
        copy=False,
        help="Availability Start Date",
    )
    expected_price = fields.Float(required=True, default=0, help="Expected price of the Property")
    selling_price = fields.Float(readonly=True, copy=False, help="Selling price of the Property")
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer("Living area (sqm)", default=0)
    facades = fields.Integer(default=0)
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer("Garden_area (sqm)", default=0)
    garden_orientation = fields.Selection(
        selection=_garden_orientation_list,
        help="Type is used to set the garden orientation",
    )
    state = fields.Selection(selection=_state_list, default="new", string="Status", required=True, copy=False)
    active = fields.Boolean(default=True)

    # Relational
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer_id = fields.Many2one("res.partner", string="Buyer", readonly=True, copy=False)
    user_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")

    # Computed
    total_area = fields.Integer(
        string="Total Area (sqm)",
        compute="_compute_total_area",
        help="Total area computed with the living_area and the garden_area",
    )
    best_price = fields.Float("Best Offer", compute="_compute_best_price", help="Best offer received")

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for line in self:
            line.total_area = line.living_area + line.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for line in self:
            line.best_price = max(line.offer_ids.mapped("price")) if line.offer_ids else 0.0

    # Onchanges
    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "N"
        else:
            self.garden_area = 0
            self.garden_orientation = False
