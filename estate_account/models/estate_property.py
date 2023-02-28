# -*- coding: utf-8 -*-

from odoo import models, Command


class EstateProperty(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "estate.property"

    # ---------------------------------------- Action Methods -------------------------------------

    def action_sold(self):
        res = super().action_sold()
        for record in self:
            values = {
                "partner_id": record.buyer_id.id,
                "move_type": "out_invoice",
            }
            self.env["account.move"].create(values)
        return res
