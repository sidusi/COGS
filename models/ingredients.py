from odoo import models, fields, api


class Ingredients(models.Model):
    _name = 'cogs.ingredients'
    _description = 'COGS Ingredients'

    name = fields.Char(string="Ingredients Name", required=True)
    ingredients_category = fields.Many2one('cogs.ingredient.categories', string="Ingredients Category", required=True)
    price = fields.Float(string="Ingredients Price", required=True)
    netto = fields.Integer(string="Netto/Net Weight", required=True)
    uom = fields.Many2one('cogs.ingredient.uom', string="Unit of Measure(UoM)", required=True)



class IngredientCategory(models.Model):
    _name = 'cogs.ingredient.categories'
    _description = 'COGS Ingredient Categories'

    name = fields.Char(string="Category Name", required=True)


class Uom(models.Model):
    _name = 'cogs.ingredient.uom'
    _description = 'COGS ingredient UoM'

    code = fields.Char(string="UoM Code", required=True)
    name = fields.Char(string="UoM Name", required=True)
