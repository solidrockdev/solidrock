from odoo import fields, models, api


class Customer(models.Model):
    '''
        Inherit partner module to create a new customized customer module
    '''
    _name = 'my.customer'
    _inherits = {'res.partner': 'partner_id'}

    customer_type = fields.Many2one('my.customer.type',string="Customer Type")
    first_name = fields.Char(string="First Name")
    middle_initial = fields.Char(string="Middle Initial")
    last_name = fields.Char(string="Last Name")
    primary_contact = fields.Char(string="Primary Contact")
    secondary_contact = fields.Char(string="Secondary Contact")
    balance = fields.Float()
    balance_total = fields.Float()
    terms_id = fields.Many2one('account.payment.term', string="Terms")
    tax_code = fields.Integer(string="Tax Code")
    tax_item = fields.Many2one('account.tax', string="Tax Item")
    rep_id = fields.Many2one('hr.employee', string="Rep")
    resale = fields.Char()
    account = fields.Char()
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
    state_id_ship  = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")
    country_id_ship  = fields.Many2one('res.country', string='Country', ondelete='restrict')
    country_code_ship  = fields.Char(related='country_id.code', string="Country Code")


    def action_open_employees(self):
        return



class CustomerType(models.Model):
    '''
        Inherit partner module to create a new customized customer module
    '''
    _name = 'my.customer.type'

