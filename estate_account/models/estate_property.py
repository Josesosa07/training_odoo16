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
            create_invoice_line = [
                self.create_line(record.name, 1.0, record.selling_price * 6.0 / 100.0),
                self.create_line("Administrative fees", 1.0, 100.0),
            ]
            values = {
                "partner_id": record.buyer_id.id,
                "move_type": "out_invoice",
                "journal_id": journal.id,
                "invoice_line_ids": create_invoice_line,
            }
            self.env["account.move"].create(values)
        return res

    def create_line(self, name, quantity, unit_price):
        return Command.create(
            {
                "name": name,
                "quantity": quantity,
                "price_unit": unit_price,
            }
        )
