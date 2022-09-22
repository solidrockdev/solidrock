from odoo import fields, models, api


class Customer(models.Model):
    '''
        Inherit partner module to create a new customized customer module
    '''
    _name = 'my.customer'
    _inherits = {'res.partner': 'partner_id'}

    customer_type = fields.Many2one('my.customer.type',string="Customer Type")
    company = fields.Char(string="Company")
    first_name = fields.Char(string="First Name")
    middle_initial = fields.Char(string="Middle Initial")
    last_name = fields.Char(string="Last Name")
    primary_contact = fields.Char(string="Primary Contact")
    secondary_contact = fields.Char(string="Secondary Contact")
    balance = fields.Float()
    balance_total = fields.Float()
    terms_id = fields.Many2one('account.payment.term', string="Terms")
    tax_code = fields.Char(string="Tax Code")
    tax_item = fields.Many2one('account.tax', string="Tax Item")
    rep_id = fields.Many2one('hr.employee', string="Rep")
    resale = fields.Char()
    account_no = fields.Char()
    job_status = fields.Char()
    job_type = fields.Selection([('commercial', 'Commercial'), ('residential', 'Residential')], string="Job Type")
    job_description = fields.Text()
    start_date = fields.Date()
    projected_end = fields.Date()
    end_date = fields.Date()
    street_ship = fields.Char()
    street2_ship = fields.Char()
    zip_ship = fields.Char(change_default=True)
    city_ship = fields.Char()
    state_id_ship = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")
    country_id_ship = fields.Many2one('res.country', string='Country', ondelete='restrict')
    country_code_ship = fields.Char(related='country_id.code', string="Country Code")
    fax = fields.Char()

    # fields for smart buttons
    sale_order_count = fields.Integer()
    purchase_order_count = fields.Integer()
    total_invoiced = fields.Integer()
    currency_id = fields.Integer()
    open_partner_ledger = fields.Integer()
    supplier_invoice_count = fields.Integer()
    # task_count = fields.Integer()

    # product_details_ids = fields.One2many('product.detail', 'product_stock_id', string='Stock')
    # product_detail_id = fields.One2many('product.detail', 'product_stocks_ids', string='Stock')
    product_detail_ids = fields.One2many('product.info', 'stockss_id', string='Stock')


    # Farm Equipment Base model

class ProductDetails(models.Model):
    _name = 'product.info'

    name_id = fields.Many2one('product.template',ondelete='restrict', index=True,)
    product_category_id = fields.Many2one('product.category', ondelete='restrict', index=True, )
    warranty_start_date = fields.Date(string="Start Date")
    warranty_end_date = fields.Date(string="Warranty End Date")
    expiration_date = fields.Date(string="Expiration Date")
    product_stock_id = fields.Many2one('my.customer')
    stockss_id = fields.Many2one('my.customer')
    # product_stocks_ids = fields.Many2one('my.customer')

    @api.onchange('name_id')
    def onchange_skus(self):
        for record in self:
            skus = self.env['product.template'].search(
                [('id', '=', record.name_id.id), ('name', '=', record.name_id.name)], limit=1)
            record.product_category_id = skus.categ_id.id
            record.warranty_start_date = skus.warranty_start_date
            record.warranty_end_date = skus.warranty_end_date
            record.expiration_date = skus.expiration_date

class SkuDetails(models.Model):
    _name = 'sku.details'

    name = fields.Char()
    warranty_start_date = fields.Date(string="Start Date")




    # def action_open_employees(self):
    #     return
    # def project_task_action_from_partner(self):
    #     print('----------')




class CustomerType(models.Model):
    '''
        Inherit partner module to create a new customized customer module
    '''
    _name = 'my.customer.type'


# class ResPartner(models.Model):
#     """ Inherits partner and adds Tasks information in the partner form """
#     _inherit = 'res.partner'
#
#     task_ids = fields.One2many('project.task', 'partner_id', string='Tasks')
#     task_count = fields.Integer(compute='_compute_task_count', string='# Tasks')
#
#     def _compute_task_count(self):
#         fetch_data = self.env['project.task'].read_group([('partner_id', 'in', self.ids)], ['partner_id'], ['partner_id'])
#         result = dict((data['partner_id'][0], data['partner_id_count']) for data in fetch_data)
#         for partner in self:
#             partner.task_count = result.get(partner.id, 0) + sum(c.task_count for c in partner.child_ids)



