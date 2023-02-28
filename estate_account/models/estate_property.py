# -*- coding: utf-8 -*-

from odoo import models, Command


class EstateProperty(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "estate.property"

    # ---------------------------------------- Action Methods -------------------------------------

    def action_sold(self):
        res = super().action_sold()
        journal = self.env["account.journal"].search([("type", "=", "sale")], limit=1)
        for record in self:
            values = {
                "partner_id": record.buyer_id.id,
                "move_type": "out_invoice",
                "journal_id": journal.id,
            }
            moves = self.env["account.move"].create(values)
        return res
