# -*- coding: utf-8 -*-

from flectra import fields, models, _, api

class ProductProductSuggestion(models.Model):
    _inherit = 'product.product'

    suggested_product_ids = fields.Many2many('product.template', string="Productos Sugeridos")

