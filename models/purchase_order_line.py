# -*- coding: utf-8 -*-

from flectra import fields, models, _, api
import logging

_logger = logging.getLogger(__name__)
class PurchaseOrderLineSuggestion(models.Model):
    _inherit = 'purchase.order.line'

    def do_change(self):
        _logger.info(_(f"Logging -------->{self.name}------{self.id}-------"))

