from odoo import models, fields, api


class MeasuringSpoon(models.Model):
    _name = 'cogs.measuring.spoon'
    _description = 'COGS Measuring Spoon'

    name = fields.Char(string="Name")
    ingredient_ids = fields.Many2one('cogs.ingredients', string="Measuring Of")
    uom_ids = fields.Many2one('cogs.ingredient.uom', string="UoM Code")
    gram_unit = fields.Float(string="Gram Unit", required=True)
