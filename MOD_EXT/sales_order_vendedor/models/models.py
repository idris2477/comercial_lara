# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    vendedor_producto = fields.Many2one(comodel_name='res.partner', string='Vendedor')