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
    '''
           Inherit res.Partner model to create a new customized customer module
    '''

    _inherit = "res.partner"

    '''Added a checkbox in customer form view'''

    primary_billing_contact = fields.Boolean('Primary Billing Contact', default=True)

    '''Changed the company type default from company to individual'''

    company_type = fields.Selection(string='Company Type', selection=[('person', 'Individual'), ('company', 'Company')],
                                    compute='_compute_company_type', inverse='_write_company_type', default='person')

    # customer_type = fields.Many2one('my.customer.type',string="Customer Type")
    customer_type = fields.Selection(
        [('influencers', 'Influencers'),
         ('precision_dealers', 'Precision Dealers'),
         ('employees', 'Employees'),
         ('partners', 'Partners'),
         ('distant_customers', 'Distant Customers'),
         ('peterson_ag_customers', 'Peterson Ag Customers'),
         ('retired', 'Retired'),
         ('hoosier_customer', 'Hoosier Customer'),
         ('unsubscribed', 'Unsubscribed'),
         ('other', 'Other'),
         ], string='Customer Type')
    # vendor_type = fields.Many2one('my.vendor.type',string="Vendor Type")
    vendor_type = fields.Selection(
        [('top_tier', 'Top Tier'),
         ('oem_dealer', 'OEM/Dealer'),
         ('other', 'Other'),
         ('partner', 'Partner'),
         ('precision_dealer', 'Precision Dealer'),
         ], string='Vendor Type')
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

    '''Changed job position as a selection field'''

    function_s = fields.Selection(
        [('owner', 'Owner'),
         ('mechanic', 'Mechanic'),
         ('salesman', 'Salesman'),
         ('manager', 'Manager'),
         ], string='Job Position')

    function_st = fields.Selection(
        [('agronomist', 'Agronomist'),
         ('engineer', 'Engineer'),
         ('owner', 'Owner'),
         ('salesrep', 'Sales Rep'), ('techsupport', 'Technical Support'),
         ], string='Job Position')

    '''Added fields for MISC tab'''
    resale = fields.Char()
    account_no = fields.Char()
    job_status = fields.Char()
    job_type = fields.Selection([('commercial', 'Commercial'), ('residential', 'Residential')], string="Job Type")
    job_description = fields.Text()
    start_date = fields.Date()
    projected_end = fields.Date()
    end_date = fields.Date()

    '''Added for Farm Equipment tab'''

    planter_company_id = fields.Char(string="Make")
    planter_serial_no = fields.Char(string='Serial No')
    planter_model = fields.Char(string="Model", readonly=False)
    planter_year = fields.Char(string="Year", readonly=False)
    planter_rows = fields.Char(string="Rows", readonly=False)
    planter_crops_being_planted = fields.Char(string="Crops being planted", readonly=False)  # many2many
    planter_acres_planted_per_year = fields.Char(string="Acres Planted Per Year", readonly=False)
    planter_spacing = fields.Char(string="Spacing", readonly=False)
    planter_frame_type = fields.Char(string="Frame Type", readonly=False)  # many2one
    planter_seed_delivery = fields.Char(string="Seed Delivery", readonly=False)
    planter_original_planter_monitor = fields.Char(string="Original Planter Monitor", readonly=False)
    planter_current_planter_monitor = fields.Char(string="Current Planter Monitor", readonly=False)
    planter_meter_type = fields.Char(string="Meter Type", readonly=False)  # many2one
    planter_meter_drive_system = fields.Char(string="Meter Drive System", readonly=False)  # many2one
    planter_closing_system = fields.Char(string="Closing System", readonly=False)  # many2one
    planter_hopper_type = fields.Char(string="Hopper Type", readonly=False)  # many2one
    planter_row_config = fields.Char(string="Row Configuration", readonly=False)
    planter_no_of_regular_parallel_arms = fields.Char(string="No of Regular Parallel Arms", readonly=False)
    planter_no_of_long_parallel_arms = fields.Char(string="No of Long Parallel Arms", readonly=False)
    planter_downforce_system = fields.Char(string="Down Force System", readonly=False)
    planter_no_of_vr_motors = fields.Char(string="No of VR Motors", readonly=False)
    planter_row_cleaner_make = fields.Char(string="Row Cleaner Make", readonly=False)
    planter_row_cleaner_model = fields.Char(string="Row Cleaner Model", readonly=False)
    planter_no_till_coulters = fields.Char(string="No-Till Coulters", readonly=False)
    planter_liquid_application_method_1 = fields.Char(string="Liquid Application Method #1", readonly=False)  # many2one
    planter_liquid_application_method_2 = fields.Char(string="Liquid Application Method #2", readonly=False)  # many2one
    planter_firmer = fields.Char(string="Firmer", readonly=False)
    planter_gps_make = fields.Char(string="GPS Make", readonly=False)
    planter_gps_monitor = fields.Char(string="GPS Monitor", readonly=False)

    tractor_company_id = fields.Char(string="Make")
    tractor_model = fields.Char(string="Model", readonly=False)
    tractor_year = fields.Char(string="Year", readonly=False)
    tractor_no_of_hydraulic_remotes = fields.Char(string="No of Hydraulic Remotes", readonly=False)
    tractor_hydraulic_capacity = fields.Char(string="Hydraulic Capacity", readonly=False)

    combine_company_id = fields.Char(string="Make")
    combine_model = fields.Char(string="Model", readonly=False)
    combine_year = fields.Char(string="Year", readonly=False)
    combine_no_of_hydraulic_remotes = fields.Char(string="No of Hydraulic Remotes", readonly=False)
    combine_hydraulic_capacity = fields.Char(string="Hydraulic Capacity", readonly=False)

    combine_head_company_id = fields.Char(string="Make")
    combine_head_model = fields.Char(string="Model", readonly=False)
    combine_head_year = fields.Char(string="Year", readonly=False)

    sprayer_company_id = fields.Char(string="Make")
    sprayer_model = fields.Char(string="Model", readonly=False)
    sprayer_year = fields.Char(string="Year", readonly=False)
    sprayer_width = fields.Char(string="Width", readonly=False)
    sprayer_monitor = fields.Char(string="Monitor", readonly=False)
    sprayer_spacing = fields.Char(string="Spacing", readonly=False)



    warranty_start_date = fields.Date(string="Warranty Start Date", readonly=False)
    warranty_end_date = fields.Date(string="Warranty End Date", readonly=False)
    expiration_date = fields.Date(string="Expiration Date", readonly=False)
    is_farm_equipment_base = fields.Boolean(string="Is Farm Equipment Base", default=False, readonly=False)
    customer = fields.Many2one('res.partner', string="Customer", readonly=False)
    mpn = fields.Char(string="MPN")
    tax_agency = fields.Char(string="Tax Agency")
    assets_account = fields.Many2one('account.account', string='Assets Account')
    accumulated_depreciation = fields.Float(string='Accumulated Depreciation')
    # serial_no = fields.Many2many('stock.production.lot', 'contact_product_serial_no', string='Serial No')
    preferred_vendor = fields.Many2one('res.partner', string="Preferred Vendor")
    # reorder_pt_min = fields.Float(string='Reorder Pt (Min)')
    # reorder_pt_max = fields.Float(string='Max')
    tax_status = fields.Selection([
        ('tax', 'Tax'),
        ('non', 'Non'),
        ('yes', 'Yes'),
    ], default='non', string="Tax Status")










    '''Added fields for customer discounts tab'''

    # customer_base_discount = fields.Float()
    # customer_early_order_discount = fields.Float()
    # customer_early_pay_discount = fields.Float()
    # early_order_deadline = fields.Date()

    primary_contact = fields.Char(string="Primary Contact")
    fax = fields.Char(string="Fax")
    support_mobile = fields.Char(string="Support Phone")
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
    date_added = fields.Date(string="Date Added", default=fields.Date.context_today)
    dob = fields.Date(string="Date of Birth")
    from_timer = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="From Timer")
    attach = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Attach")
    eligible_for_1099 = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Eligible For 1099")
    print_on_check_as = fields.Char(string="Print on Cheque As")
    notes = fields.Selection([('has_notes', 'Has Notes'), ('no_notes', 'No Notes')], string="Notes", default="has_notes")
    role = fields.Char(string="Role Description")
    level1_free_ship_volume = fields.Float(string="Level 1 Free Shipping Volume")
    level2_free_ship_volume = fields.Float(string="Level 2 Free Shipping Volume")
    level1_free_ship_date_start = fields.Date(string="Level 1 Free Shipping Date Range Start")
    level1_free_ship_date_end = fields.Date(string="Level 1 Free Shipping Date Range End")
    level2_free_ship_date_start = fields.Date(string="Level 2 Free Shipping Date Range Start")
    level2_free_ship_date_end = fields.Date(string="Level 2 Free Shipping Date Range End")
    level2_date_range_start = fields.Date(string="Level 2 Date Range Start")
    level2_date_range_end = fields.Date(string="Level 2 Date Range End")
    level3_date_range_start = fields.Date(string="Level 3 Date Range Start")
    level3_date_range_end = fields.Date(string="Level 3 Date Range End")
    db_free_freight_date_range_start = fields.Date(string="Free Freight Start Date")
    db_free_freight_date_range_end = fields.Date(string="Free Freight End Date")
    additional_notes = fields.Text(string="Additional Notes")


    ''' 
        Added customer and vendor radio buttons
    '''
    is_customer_vendor = fields.Selection(string='Contact Type', selection=[('is_customer', 'Customer'), ('is_vendor', 'Vendor')], default='is_customer')
    is_date_based_disc = fields.Selection(selection=[('yes', 'Yes'), ('no', 'No')], string="Date Based Discounts", default='no')
    is_vol_based_disc = fields.Selection(selection=[('yes', 'Yes'), ('no', 'No')], string="Volume Based Discounts", default='no')
    # is_cus_based_disc = fields.Selection(selection=[('yes', 'Yes'), ('no', 'No')], string="Customer Discounts", default='no')


    db_std_base_dealer_disc = fields.Float(string="Standard Base Dealer Discount")
    db_level_2_disc = fields.Float(string="Level 2 Discount")
    db_level_3_dealer_disc = fields.Float(string="Level 3 Dealer Discount")
    db_free_freight_vol = fields.Float(string="Free Freight Volume")
    additional_notes = fields.Text(string="Additional Notes")


    '''For adding currency symbol in volume based margin tab'''

    company_currency_id = fields.Many2one("res.currency",related="company_id.currency_id", string="Company Currency", readonly=True,
                                          store=True, default=lambda self:
                                self.env['res.currency'].search([('name','=','USD')],limit=1))

    vb_volume_disc_level_1 = fields.Float(string="Volume Discount Level 1")
    vb_level_1_disc = fields.Float(string="Level 1 Discount")
    vb_volume_disc_level_2 = fields.Float(string="Volume Discount Level 2")
    vb_level_2_disc = fields.Float(string="Level 2 Discount")
    vb_volume_disc_level_3 = fields.Float(string="Volume Discount Level 3")
    vb_level_3_disc = fields.Float(string="Level 3 Discount")
    vb_volume_disc_level_4 = fields.Float(string="Volume Discount Level 4")
    vb_level_4_disc = fields.Float(string="Level 4 Discount")

    '''for contact and address tab'''
    contact_name1 = fields.Many2one('res.partner', string="Contact")


    contact_name = fields.Many2one('res.partner',string="Contact")
    first_name1 = fields.Char(string="First Name")
    middle_initial1 = fields.Char(string="Middle Initial")
    last_name1 = fields.Char(string="Last Name")
    role1 = fields.Char(string="Role")
    job_title = fields.Char(string="Job Title")
    mobile1 = fields.Char(string="Mobile")
    work_phone1 = fields.Char(string="Work Phone")
    home_phone1 = fields.Char(string="Home Phone")
    email1 = fields.Char(string="Email")
    street_contact2 = fields.Char()
    street2_contact2 = fields.Char()
    zip_contact2 = fields.Char(change_default=True)
    city_contact2 = fields.Char()
    state_id_contact2 = fields.Many2one("res.country.state", string='State', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
    country_id_contact2 = fields.Many2one('res.country', string='Country', ondelete='restrict')




    @api.onchange('contact_name')
    def onchange_contact(self):
        if self.contact_name:
            print(self.contact_name)
            contact = self.env['res.partner'].search([('id', '=', self.contact_name.id)])
            print(contact)
            print(contact.first_name)
            self.first_name1 = contact.first_name
            self.middle_initial1 = contact.middle_initial
            self.last_name1 = contact.last_name
            self.role1 = contact.role
            self.job_title = contact.function
            self.mobile1 = contact.mobile
            self.work_phone1 = contact.work_phone
            self.home_phone1 = contact.home_phone
            self.email1 = contact.email
            self.street_contact2 = contact.street
            self.street2_contact2 = contact.street2
            self.zip_contact2 = contact.zip
            self.city_contact2 = contact.city
            self.state_id_contact2 = contact.state_id
            self.country_id_contact2 = contact.country_id


    '''For addresses and contact tab when contact name is selected all the corresponding fields will autopopulate'''

    @api.onchange('contact_name1')
    def onchange_contact1(self):
        if self.contact_name1:
            print(self.contact_name1)
            contact = self.env['res.partner'].search([('id', '=', self.contact_name1.id)])
            print(contact)
            print(contact.first_name)
            self.name = contact.first_name
            self.middle_initial = contact.middle_initial
            self.last_name = contact.last_name
            self.role = contact.role
            self.function = contact.function
            self.mobile = contact.mobile
            self.phone = contact.work_phone
            self.home_phone1 = contact.home_phone
            self.email = contact.email
            self.street = contact.street
            self.street2 = contact.street2
            self.zip = contact.zip
            self.city = contact.city
            self.state_id = contact.state_id
            self.country_id = contact.country_id


    '''For customer and vendor radio button, when a radio button is selected its corresponding fields will be visible'''
    @api.onchange('is_customer_vendor')
    def onchange_customer(self):
        if self.is_customer_vendor == 'is_customer':
            self.supplier_rank = 0
            self.customer_rank = 1
        else:
            self.supplier_rank = 1
            self.customer_rank = 0



''' 
    
    Farm Equipment Base model
'''




class ProductDetails(models.Model):
    _name = 'product.info'

    company_id = fields.Many2one('res.company', 'Company', index=1, readonly=False)
    partner_id = fields.Many2one('res.partner', readonly=False)
    warranty_start_date = fields.Date(string="Warranty Start Date", readonly=False)
    warranty_end_date = fields.Date(string="Warranty End Date", readonly=False)
    expiration_date = fields.Date(string="Expiration Date", readonly=False)
    is_farm_equipment_base = fields.Boolean(string="Is Farm Equipment Base", default=False, readonly=False)
    customer = fields.Many2one('res.partner', string="Customer", readonly=False)
    model = fields.Char(string="Model", readonly=False)
    year = fields.Char(string="Year", readonly=False)
    rows = fields.Integer(string="Rows", readonly=False)
    crops_being_planted = fields.Char(string="Crops being planted", readonly=False)  # many2many
    acres_planted_per_year = fields.Char(string="Acres Planted Per Year", readonly=False)
    spacing = fields.Integer(string="Spacing", readonly=False)
    frame_type = fields.Char(string="Frame Type", readonly=False)  # many2one
    seed_delivery = fields.Char(string="Seed Delivery", readonly=False)
    original_planter_monitor = fields.Char(string="Original Planter Monitor", readonly=False)
    current_planter_monitor = fields.Char(string="Current Planter Monitor", readonly=False)
    meter_type = fields.Char(string="Meter Type", readonly=False)  # many2one
    meter_drive_system = fields.Char(string="Meter Drive System", readonly=False)  # many2one
    closing_system = fields.Char(string="Closing System", readonly=False)  # many2one
    hopper_type = fields.Char(string="Hopper Type", readonly=False)  # many2one
    row_config = fields.Char(string="Row Configuration", readonly=False)
    no_of_regular_parallel_arms = fields.Integer(string="No of Regular Parallel Arms", readonly=False)
    no_of_long_parallel_arms = fields.Integer(string="No of Long Parallel Arms", readonly=False)
    downforce_system = fields.Char(string="Down Force System", readonly=False)
    no_of_vr_motors = fields.Integer(string="No of VR Motors", readonly=False)
    row_cleaner_make = fields.Char(string="Row Cleaner Make", readonly=False)
    row_cleaner_model = fields.Char(string="Row Cleaner Model", readonly=False)
    no_till_coulters = fields.Char(string="No-Till Coulters", readonly=False)
    liquid_application_method_1 = fields.Char(string="Liquid Application Method #1", readonly=False)  # many2one
    liquid_application_method_2 = fields.Char(string="Liquid Application Method #2", readonly=False)  # many2one
    firmer = fields.Char(string="Firmer", readonly=False)
    gps_make = fields.Char(string="GPS Make", readonly=False)
    gps_monitor = fields.Char(string="GPS Monitor", readonly=False)
    no_of_hydraulic_remotes = fields.Integer(string="No of Hydraulic Remotes", readonly=False)
    hydraulic_capacity = fields.Char(string="Hydraulic Capacity", readonly=False)
    width = fields.Float(string="Width", readonly=False)
    monitor = fields.Char(string="Monitor", readonly=False)
    mpn = fields.Char(string="MPN")
    tax_agency = fields.Char(string="Tax Agency")
    assets_account = fields.Many2one('account.account', string='Assets Account')
    accumulated_depreciation = fields.Float(string='Accumulated Depreciation')
    # serial_no = fields.Many2many('stock.production.lot', 'contact_product_serial_no', string='Serial No')
    preferred_vendor = fields.Many2one('res.partner', string="Preferred Vendor")
    # reorder_pt_min = fields.Float(string='Reorder Pt (Min)')
    # reorder_pt_max = fields.Float(string='Max')
    tax_status = fields.Selection([
        ('tax', 'Tax'),
        ('non', 'Non'),
        ('yes', 'Yes'),
    ], default='non', string="Tax Status")
    serial_no = fields.Many2many('stock.production.lot', 'contact_product_serial_no', string='Serial No',
                                 compute='_compute_serial_no', readonly=False)


    # @api.onchange('name_id')
    # def onchange_skus(self):
    #     for record in self:
    #         # print(record.id)
    #         skus = self.env['product.template'].search(
    #             [('id', '=', record.name_id.id), ('name', '=', record.name_id.name)], limit=1)
    #         record.product_category_id = skus.categ_id.id
    #         record.warranty_start_date = skus.warranty_start_date
    #         record.warranty_end_date = skus.warranty_end_date
    #         record.expiration_date = skus.expiration_date
    #         record.company_id = skus.company_id
    #         record.model = skus.model
    #         record.year = skus.year
    #         record.partner_id = record.id
    #         record.serial_no = skus.serial_no









class SkuDetails(models.Model):
    _name = 'sku.details'

    name = fields.Char()
    warranty_start_date = fields.Date(string="Start Date")





# class CustomerType(models.Model):
    '''
        for the  field customer_type in customer form
    '''
    # _name = 'my.customer.type'
    # name = fields.Char()




# class VendorType(models.Model):
    '''
        for the field vendor_type in vendor form
    '''
    # _name = 'my.vendor.type'
    # name = fields.Char()


class InvoiceInherit(models.Model):
    '''
           Inherit account.Move model
    '''

    _inherit = "account.move"

    estimate = fields.Monetary(string="Estimate")


class InvoiceInheritLine(models.Model):
    '''
           Inherit account.Move.line model
    '''

    _inherit = "account.move.line"

    so_no = fields.Char(string="S.O.No.")

class PurchaseorderInherit(models.Model):
        '''
               Inherit purchase.Order model
        '''

        _inherit = "purchase.order"

        customer = fields.Char(string="Customer")

class PurchaseOrderLineInherit(models.Model):
    '''
           Inherit Purchase.Order.line model
    '''

    _inherit = "purchase.order.line"

    mpn = fields.Char(string="MPN")



