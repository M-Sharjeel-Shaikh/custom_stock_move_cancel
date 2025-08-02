from odoo import api, fields, models
from odoo.exceptions import UserError

class StockMove(models.Model):
    _inherit = 'stock.move'

    def bulk_stock_move_line_cancel(self):
        for move in self:
            if move.state == 'done':
                raise UserError("You cannot cancel a completed move. Please reverse it using a return or scrap.")
            if move.state not in ['draft', 'confirmed', 'assigned']:
                raise UserError("Only draft, confirmed or assigned moves can be cancelled.")

            # Unreserve stock
            if move.state == 'assigned':
                move._do_unreserve()

            # Cancel move
            move.state = 'cancel'


    def bulk_stock_move_line_cancel_reset(self):
        for move in self:
            if move.state != 'cancel':
                raise UserError("Only canceled moves can be reset to draft.")
            move.write({'state': 'draft'})
