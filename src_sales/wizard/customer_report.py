from odoo import api, fields, models

class CustomerReportWizard(models.TransientModel):
    _name = "customer.report.wizard"
    _description = "Customer Report Wizard"

    # employee_id =fields.text()

    def action_print_report(self):
        return {

            'type': 'ir.actions.report',
            'report_name': 'src_sales.report_customer_transaction',
            'model': 'customer.report.wizard',
            'report_type': "qweb-pdf",

        }
        # return