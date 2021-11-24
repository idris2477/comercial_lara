# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_eje = fields.Many2one('product.eje', string='Eje')
    product_montaje = fields.Many2one('product.montaje', string='Lado Montaje')
    product_medida = fields.Many2one('product.medida', string='Medida')
    product_marca_vehiculo = fields.Many2one('product.marca.vehiculo', string='Marca Vehiculo')
    product_modelo = fields.Many2one('product.modelo', string='Modelo Carro')
    product_motor = fields.Many2one('product.motor', string='Motor Cilindro')
    product_observacion = fields.Many2one('product.observacion', string='Observacion')
    product_numero_parte = fields.Char(string='Número de Parte')
    product_year = fields.Char(string='Fecha Desde')
    product_year_hasta = fields.Char(string='Fecha Hasta')

class ProductEje(models.Model):
    _name = "product.eje"

    name = fields.Char(string="Eje")


class ProductLadoMontaje(models.Model):
    _name = "product.montaje"

    name = fields.Char(string="Lado Monaje")


class ProductMedida(models.Model):
    _name = "product.medida"

    name = fields.Char(string="Medida")


class ProductMarcaVehiculo(models.Model):
    _name = "product.marca.vehiculo"

    name = fields.Char(string="Marca Vehiculo")


class ProductModelo(models.Model):
    _name = "product.modelo"

    name = fields.Char(string="Modelo Carro")


class ProductMotor(models.Model):
    _name = "product.motor"

    name = fields.Char(string="Motor Cilindro")


class Observacion(models.Model):
    _name = "product.observacion"

    name = fields.Char(string="Observacion")

#
# class ProductYear(models.Model):
#     _name = "product.year"
#
#     name = fields.Char(string="Fecha Desde")
#
#
# class ProductYearhasta(models.Model):
#     _name = "product.year.hasta"
#
#     name = fields.Char(string="Fecha Hasta")





