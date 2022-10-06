# -*- coding: utf-8 -*-
# from odoo import http


# class SrcFieldService(http.Controller):
#     @http.route('/src_field_service/src_field_service', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/src_field_service/src_field_service/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('src_field_service.listing', {
#             'root': '/src_field_service/src_field_service',
#             'objects': http.request.env['src_field_service.src_field_service'].search([]),
#         })

#     @http.route('/src_field_service/src_field_service/objects/<model("src_field_service.src_field_service"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('src_field_service.object', {
#             'object': obj
#         })
