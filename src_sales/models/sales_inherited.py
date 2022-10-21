from odoo import fields, models, api

class SaleInherited(models.Model):
    '''
               Inherit sale.order model to create a new customized sale module
        '''

    _inherit = "sale.order"



# class SaleOrderLineInherited(models.Model):
#     '''
#                Inherit sale.order model to create a new customized sale module
#         '''
#
#     _inherit = "sale.order.line"
#
#     available_qty = fields.Float(compute='_compute_available_count', string='Available Qty')
#
#     @api.depends('product_id')
#     def _compute_available_count(self):
#         for rec in self:
#             rec.available_qty = rec.qty_available
