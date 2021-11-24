# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    marca_producto = fields.Char(string="Marca")
    eje = fields.Char(string="Eje")
    lado_montaje = fields.Char(string="Lado de Montaje")
    medida = fields.Char(string="Medidas")
    marca_vehiculo = fields.Char(string="Marca del Vehículo")
    modelo_carro = fields.Char(string="Modelo")
    motor_cilindro = fields.Char(string="Motor Cilindro")
    fecha_inicio = fields.Char(string="Desde")
    fecha_final = fields.Char(string="Hasta")
    observacione = fields.Char(string="Observación")


