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
    # --------------------------------------- Private Attributes ----------------------------------

    _name = "estate.property"
    _description = "Real Estate Property"

    # --------------------------------------- Fields Declaration ----------------------------------
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
