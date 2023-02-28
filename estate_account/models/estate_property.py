# -*- coding: utf-8 -*-

from odoo import models, Command


class EstateProperty(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "estate.property"

    # ---------------------------------------- Action Methods -------------------------------------

    def action_sold(self):
        res = super().action_sold()
        return res
