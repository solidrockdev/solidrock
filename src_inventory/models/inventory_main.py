from odoo import models, fields, api


class Inventorys(models.Model):
    '''
           Inherit product.template model to create a new customized inventory module
    '''

    _inherit = "product.template"

    warranty_start_date = fields.Date(string="Warranty Start Date")
    warranty_end_date = fields.Date(string="Warranty End Date")
    expiration_date = fields.Date(string="Expiration Date")
    is_farm_equipment_base = fields.Boolean(string="Is Farm Equipment Base", default=False)
    customer = fields.Many2one('res.partner', string="Customer")





