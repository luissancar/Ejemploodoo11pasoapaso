from odoo import models, fields, api

class Dato(models.Model):
    _name = 'prue01.dato'
    codigo = fields.Integer('Codigo', required=True)
    marca = fields.Char('Marca', required=True)