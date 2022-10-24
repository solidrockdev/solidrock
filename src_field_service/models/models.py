# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class src_field_service(models.Model):
#     _name = 'src_field_service.src_field_service'
#     _description = 'src_field_service.src_field_service'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
