# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    vendedor_producto = fields.Many2one('res.partner', string='Vendedor')
    vendedor_aux = fields.Many2one('res.partner', compute='_compute_vendedor')

    def _compute_vendedor(self):
        self.vendedor_aux = ""
        vendedor = self.env['sale.order'].search([('name', '=', self.invoice_origin)])
        if vendedor:
            for red in vendedor:
                self.vendedor_aux = red.vendedor_producto.id
                self.vendedor_producto = self.vendedor_aux


class AccountMove(models.Model):
    _inherit = 'account.move'

    prueba_switches = fields.Boolean(defaul=False, value=False)

    @api.onchange('act_nota_entre')
    def _onchage_checks_ocultar_libros(self):
        if self.act_nota_entre == True:
            self.ocultar_libros = True
        else:
            self.ocultar_libros = False


class Partners_Report(models.Model):
    _inherit = 'res.users'

    personal_logo = fields.Binary(string='Logo Empresa')