# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from dateutil.relativedelta import relativedelta

# Available values for the garden_orientation field.
_garden_orientation_list = [("N", "North"), ("S", "South"), ("E", "East"), ("W", "West")]
_state_list = [
    ("new", "New"),
    ("offer_received", "Offer Received"),
    ("offer_accepted", "Offer Accepted"),
    ("sold", "Sold"),
    ("canceled", "Canceled"),
]


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    # name = fields.Char('Estate Property Name', required=True, translate=True)
    name = fields.Char("Title", required=True, default="Unknown")
    description = fields.Text("Description")
    postcode = fields.Char("Post Code")
    date_availability = fields.Date(
        "Available From",
        default=lambda self: (fields.Date.today() + relativedelta(months=+3)),
        copy=False,
        help="Availability Start Date",
    )
    expected_price = fields.Float("Expected Price", required=True, default=0, help="Expected price of the Property")
    selling_price = fields.Float("Selling Price", readonly=True, copy=False, help="Selling price of the Property")
    bedrooms = fields.Integer("Bedrooms", default=2)
    living_area = fields.Integer("Living area (sqm)", default=0)
    facades = fields.Integer("Facades", default=0)
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden_area (sqm)", default=0)
    garden_orientation = fields.Selection(
        selection=_garden_orientation_list,
        string="Garden Orientation",
        help="Type is used to set the garden orientation",
    )
    state = fields.Selection(selection=_state_list, default="new", string="Status", required=True, copy=False)
    active = fields.Boolean("Active", default=True)
