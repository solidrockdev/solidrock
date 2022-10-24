# -*- coding: utf-8 -*-
# from odoo import http


# class SrcCustomer(http.Controller):
#     @http.route('/src_customer/src_customer', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/src_customer/src_customer/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('src_customer.listing', {
#             'root': '/src_customer/src_customer',
#             'objects': http.request.env['src_customer.src_customer'].search([]),
#         })

#     @http.route('/src_customer/src_customer/objects/<model("src_customer.src_customer"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('src_customer.object', {
#             'object': obj
#         })
