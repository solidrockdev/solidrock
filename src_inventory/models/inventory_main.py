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
    model = fields.Char(string="Model")
    year = fields.Char(string="Year")
    rows = fields.Integer(string="Rows")
    crops_being_planted = fields.Char(string="Crops being planted") #many2many
    acres_planted_per_year = fields.Char(string="Acres Planted Per Year")
    spacing = fields.Integer(string="Spacing")
    frame_type = fields.Char(string="Frame Type") #many2one
    seed_delivery = fields.Char(string="Seed Delivery")
    original_planter_monitor = fields.Char(string="Original Planter Monitor")
    current_planter_monitor = fields.Char(string="Current Planter Monitor")
    meter_type = fields.Char(string="Meter Type") #many2one
    meter_drive_system = fields.Char(string="Meter Drive System") #many2one
    closing_system = fields.Char(string="Closing System") #many2one
    hopper_type = fields.Char(string="Hopper Type") #many2one
    row_config = fields.Char(string="Row Configuration")
    no_of_regular_parallel_arms = fields.Integer(string="No of Regular Parallel Arms")
    no_of_long_parallel_arms = fields.Integer(string="No of Long Parallel Arms")

    downforce_system = fields.Char(string="DownForce System")

    no_of_vr_motors = fields.Integer(string="No of VR Motors")
    row_cleaner_make = fields.Char(string="Row Cleaner Make")
    row_cleaner_model = fields.Char(string="Row Cleaner Model")
    no_till_coulters = fields.Char(string="No-Till Coulters")
    liquid_application_method_1 = fields.Char(string="Liquid Application Method #1") #many2one
    liquid_application_method_2 = fields.Char(string="Liquid Application Method #2") #many2one
    firmer = fields.Char(string="Firmer")
    gps_make = fields.Char(string="GPS Make")
    gps_monitor = fields.Char(string="GPS Monitor")
    no_of_hydraulic_remotes = fields.Integer(string="No of Hydraulic Remotes")
    hydraulic_capacity = fields.Char(string="Hydraulic Capacity")
    width = fields.Float(string="Width")
    monitor = fields.Char(string="Monitor")
    mpn = fields.Char(string="MPN")
    tax_agency = fields.Char(string="Tax Agency")
    assets_account = fields.Many2one('account.account',string='Assets Account')
    accumulated_depreciation = fields.Float(string='Accumulated Depreciation')
    # serial_no = fields.Many2many('stock.production.lot', 'contact_product_serial_no', string='Serial No')
    preferred_vendor = fields.Many2one('res.partner',string="Preferred Vendor")
    reorder_pt_min = fields.Float(string='Reorder Pt (Min)')
    tax_status = fields.Selection([
        ('tax', 'Tax'),
        ('non', 'Non'),
        ('yes', 'Yes'),
    ],  default='non', string="Tax Status")
    serial_no = fields.Many2many('stock.production.lot', 'contact_product_serial_no', string='Serial No', compute='_compute_serial_no')


    def _compute_serial_no(self):
        serial_nos = self.env['stock.production.lot'].search([('product_id', '=', self._origin.id)])
        list = []
        for rec in serial_nos:
            list.append(rec.id)
        self.serial_no = list

