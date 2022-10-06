from odoo import fields, models, api


# class Customer(models.Model):
#     '''
#         Inherit partner module to create a new customized customer module
#     '''
#     _name = 'my.customer'
#     _inherits = {'res.partner': 'partner_id'}

    # customer_type = fields.Many2one('my.customer.type',string="Customer Type")
    # company = fields.Char(string="Company")
    # first_name = fields.Char(string="First Name")
    # middle_initial = fields.Char(string="Middle Initial")
    # last_name = fields.Char(string="Last Name")
    # primary_contact = fields.Char(string="Primary Contact")
    # secondary_contact = fields.Char(string="Secondary Contact")
    # balance = fields.Float()
    # balance_total = fields.Float()
    # terms_id = fields.Many2one('account.payment.term', string="Terms")
    # tax_code = fields.Char(string="Tax Code")
    # tax_item = fields.Many2one('account.tax', string="Tax Item")
    # rep_id = fields.Many2one('hr.employee', string="Rep")
    # resale = fields.Char()
    # account_no = fields.Char()
    # job_status = fields.Char()
    # job_type = fields.Selection([('commercial', 'Commercial'), ('residential', 'Residential')], string="Job Type")
    # job_description = fields.Text()
    # start_date = fields.Date()
    # projected_end = fields.Date()
    # end_date = fields.Date()
    # street_ship = fields.Char()
    # street2_ship = fields.Char()
    # zip_ship = fields.Char(change_default=True)
    # city_ship = fields.Char()
    # state_id_ship = fields.Many2one("res.country.state", string='State', ondelete='restrict',
    #                            domain="[('country_id', '=?', country_id)]")
    # country_id_ship = fields.Many2one('res.country', string='Country', ondelete='restrict')
    # country_code_ship = fields.Char(related='country_id.code', string="Country Code")
    # fax = fields.Char()

    # fields for smart buttons
    # sale_order_count = fields.Integer()
    # purchase_order_count = fields.Integer()
    # total_invoiced = fields.Integer()
    # currency_id = fields.Integer()
    # open_partner_ledger = fields.Integer()
    # supplier_invoice_count = fields.Integer()
    # task_count = fields.Integer()




class PartnerInherit(models.Model):
    _inherit = "res.partner"


    customer_type = fields.Many2one('my.customer.type',string="Customer Type")
    vendor_type = fields.Many2one('my.vendor.type',string="Vendor Type")
    first_name = fields.Char(string="First Name")
    middle_initial = fields.Char(string="Middle Initial")
    last_name = fields.Char(string="Last Name")
    balance = fields.Float()
    balance_total = fields.Float()
    terms_id = fields.Many2one('account.payment.term', string="Terms")
    tax_code = fields.Char(string="Tax Code")
    tax_item = fields.Many2one('account.tax', string="Tax Item")
    rep_id = fields.Many2one('hr.employee', string="Rep")
    street_ship = fields.Char()
    street2_ship = fields.Char()
    street3 = fields.Char()
    street3_ship = fields.Char()
    zip_ship = fields.Char(change_default=True)
    city_ship = fields.Char()
    state_id_ship = fields.Many2one("res.country.state", string='State', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
    country_id_ship = fields.Many2one('res.country', string='Country', ondelete='restrict')
    resale = fields.Char()
    account_no = fields.Char()
    job_status = fields.Char()
    job_type = fields.Selection([('commercial', 'Commercial'), ('residential', 'Residential')], string="Job Type")
    job_description = fields.Text()
    start_date = fields.Date()
    projected_end = fields.Date()
    end_date = fields.Date()
    product_detail_ids = fields.One2many('product.info', 'partner_id', string='Stock')
    supplier_rank = fields.Integer(default=0, copy=False)
    customer_rank = fields.Integer(default=0, copy=False)

    primary_contact = fields.Char(string="Primary Contact")
    fax = fields.Char(string="Fax")
    work_phone = fields.Char(string="Work Phone")
    home_phone = fields.Char(string="Home Phone")
    alt_phone = fields.Char(string="Alt. Phone")
    alt_mobile = fields.Char(string="Alt. Mobile")
    linkedIn = fields.Char(string="LinkedIn")
    facebook = fields.Char(string="Facebook")
    twitter = fields.Char(string="Twitter")
    alt_email1 = fields.Char(string="Alt. Email 1")
    alt_email2 = fields.Char(string="Alt. Email 2")
    cc_email = fields.Char(string="CC Email")
    from_timer = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="From Timer")
    attach = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Attach")
    eligible_for_1099 = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Eligible For 1099")
    print_on_check_as = fields.Char(string="Print on Cheque As")
    # is_customer_vendor = fields.Selection([('is_customer', 'Customer'), ('is_vendor', 'Vendor')])
    is_customer_vendor = fields.Selection(string='Contact Type', selection=[('is_customer', 'Customer'), ('is_vendor', 'Vendor')])
    notes = fields.Selection([('has_notes', 'Has Notes'), ('no_notes', 'No Notes')], string="Notes")




    def _get_name_search_order_by_fields(self):
        res = super()._get_name_search_order_by_fields()
        partner_search_mode = self.env.context.get('res_partner_search_mode')
        if not partner_search_mode in ('customer', 'supplier'):
            return res
        order_by_field = 'COALESCE(res_partner.%s, 0) DESC,'
        if partner_search_mode == 'customer':
            field = 'customer_rank'
        else:
            field = 'supplier_rank'

        order_by_field = order_by_field % field
        return '%s, %s' % (res, order_by_field % field) if res else order_by_field



    @api.model_create_multi
    def create(self, vals_list):
        search_partner_mode = self.env.context.get('res_partner_search_mode')
        is_customer = search_partner_mode == 'customer'
        is_supplier = search_partner_mode == 'supplier'
        if search_partner_mode:
            for vals in vals_list:
                if is_customer and 'customer_rank' not in vals:
                    if self.is_customer_vendor == 'is_customer':
                        vals['customer_rank'] = 1
                elif is_supplier and 'supplier_rank' not in vals:
                    if self.is_customer_vendor == 'is_vendor' :
                        vals['supplier_rank'] = 1
        return super().create(vals_list)



# Farm Equipment Base model
class ProductDetails(models.Model):
    _name = 'product.info'

    name_id = fields.Many2one('product.template',ondelete='restrict', index=True,)
    product_category_id = fields.Many2one('product.category', ondelete='restrict', index=True, )
    warranty_start_date = fields.Date(string="Start Date")
    warranty_end_date = fields.Date(string="Warranty End Date")
    expiration_date = fields.Date(string="Expiration Date")
    # product_stock_id = fields.Many2one('my.customer')
    partner_id = fields.Many2one('res.partner')
    company_id = fields.Many2one('res.company', 'Company', index=1)
    model = fields.Char(string="Model")
    year = fields.Char(string="Year")
    serial_no = fields.Many2many('stock.production.lot', 'customer_product_serial_no', string='Serial No')
    # product_stocks_ids = fields.Many2one('my.customer')

    @api.onchange('name_id')
    def onchange_skus(self):
        for record in self:
            # print(record.id)
            skus = self.env['product.template'].search(
                [('id', '=', record.name_id.id), ('name', '=', record.name_id.name)], limit=1)
            record.product_category_id = skus.categ_id.id
            record.warranty_start_date = skus.warranty_start_date
            record.warranty_end_date = skus.warranty_end_date
            record.expiration_date = skus.expiration_date
            record.company_id = skus.company_id
            record.model = skus.model
            record.year = skus.year
            record.partner_id = record.id
            record.serial_no = skus.serial_no







class SkuDetails(models.Model):
    _name = 'sku.details'

    name = fields.Char()
    warranty_start_date = fields.Date(string="Start Date")





class CustomerType(models.Model):
    '''
        Inherit partner module to create a new customized customer module
    '''
    _name = 'my.customer.type'
    name = fields.Char()




class VendorType(models.Model):
    '''
        Inherit partner module to create a new customized customer module
    '''
    _name = 'my.vendor.type'
    name = fields.Char()
