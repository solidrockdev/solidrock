from odoo import fields, models, api


class SaleInherited(models.Model):
    '''
               Inherit sale.order model to create a new customized sale module
        '''

    _inherit = "sale.order"



class SaleOrderLineIn(models.Model):
    _inherit = 'sale.order.line'


    available_qty = fields.Float(string='Available Qty')
    product_id = fields.Many2one('product.product', string='Product')
    # order_id = fields.Many2one('sale.order', string='Order Reference', required=True, ondelete='cascade', index=True, copy=False)


    @api.onchange('product_id')
    def check_customer(self):
        self.available_qty = self.product_id.available
        # print("self.product_id.qty_available", self.product_id.available)