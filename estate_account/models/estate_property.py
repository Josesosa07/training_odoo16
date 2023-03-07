# -*- coding: utf-8 -*-

from odoo import models, Command


class EstateProperty(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "estate.property"

    # ---------------------------------------- Action Methods -------------------------------------

    def action_sold(self):
        res = super().action_sold()
        journal = self.env["account.journal"].sudo().search([("type", "=", "sale")], limit=1)
        for record in self:
            values = {
                "partner_id": record.buyer_id.id,
                "move_type": "out_invoice",
                "journal_id": journal.id,
                "invoice_line_ids": [
                    Command.create(
                        {
                            "name": record.name,
                            "quantity": 1.0,
                            "price_unit": record.selling_price * 6.0 / 100.0,
                        }
                    ),
                    Command.create(
                        {
                            "name": "Administrative fees",
                            "quantity": 1.0,
                            "price_unit": 100.0,
                        }
                    ),
                ],
            }
            self.env["account.move"].sudo().create(values)
        return res
