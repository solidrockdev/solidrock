# -*- coding: utf-8 -*-
# from odoo import http


# class SrcInventory(http.Controller):
#     @http.route('/src_inventory/src_inventory', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/src_inventory/src_inventory/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('src_inventory.listing', {
#             'root': '/src_inventory/src_inventory',
#             'objects': http.request.env['src_inventory.src_inventory'].search([]),
#         })

#     @http.route('/src_inventory/src_inventory/objects/<model("src_inventory.src_inventory"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('src_inventory.object', {
#             'object': obj
#         })
