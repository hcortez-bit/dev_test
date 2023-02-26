# -*- coding: utf-8 -*-

from flectra import fields, models, _, api
import logging

_logger = logging.getLogger(__name__)
class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'
    categ_ids = fields.Many2many('product.category', string="Categorias Permitidas")

class StockPickingSuggestion(models.Model):
    _inherit = 'stock.picking'

    categ_ids = fields.Many2many('product.category', string="Categorias Permitidas", related="picking_type_id.categ_ids")

class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.onchange('product_id')
    def _set_domain_new(self):
        categ_ids = self.picking_id.picking_type_id.mapped('categ_ids')
        res = {}
        res['domain'] = {'product_id': [('categ_id', 'in', categ_ids.ids)]}
        return res


