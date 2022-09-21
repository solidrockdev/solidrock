from odoo import models, fields, api


class Src_task(models.Model):
    '''
               Inherit field service module
    '''
    _inherit = "project.task"

    product_details_ids = fields.One2many('product.details', 'product_stock_id', string='Stock')


# Farm Equipment Base model

class Product_details(models.Model):
    _name = 'product.details'

    name_id = fields.Many2one('product.template',ondelete='restrict', index=True,)
    product_category_id = fields.Many2one('product.category', ondelete='restrict', index=True, )
    warranty_start_date = fields.Date(string="Start Date")
    warranty_end_date = fields.Date(string="Warranty End Date")
    expiration_date = fields.Date(string="Expiration Date")
    product_stock_id = fields.Many2one('project.task', index=1)

    @api.onchange('name_id')
    def onchange_skus(self):
        for record in self:
            skus = self.env['product.template'].search(
                [('id', '=', record.name_id.id), ('name', '=', record.name_id.name)], limit=1)
            record.product_category_id = skus.categ_id.id
            record.warranty_start_date = skus.warranty_start_date
            record.warranty_end_date = skus.warranty_end_date
            record.expiration_date = skus.expiration_date








