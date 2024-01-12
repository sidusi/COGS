from odoo import fields, models, api


class Recipes(models.Model):
    _name = 'cogs.recipes'
    _description = 'COGS Recipes'

    name = fields.Char(string="Recipe Name", required=True)
    recipe_categories = fields.Many2one('cogs.recipe.categories', string="Recipe Categories", required=True)
    netto = fields.Integer(string="Netto/Net Weight", required=True)
    uom = fields.Many2one('cogs.ingredient.uom', string="Unit of Measure(UoM)", required=True)
    subtotal = fields.Float(string="Subtotal")
    recipe_ingredient_ids = fields.One2many('cogs.recipe.ingredients', 'recipe_ids', string="Ingredients")


class RecipeCategories(models.Model):
    _name = 'cogs.recipe.categories'
    _description = 'COGS Recipe Categories'

    name = fields.Char(string="Recipe Categories Name", required=True)


class RecipeIngredients(models.Model):
    _name = 'cogs.recipe.ingredients'
    _description = 'COGS Ingredients for Recipes'

    name = fields.Many2one('cogs.ingredients', string="Ingredients Name")
    usage = fields.Float(string="Material Usage")
    uom = fields.Many2one('cogs.ingredient.uom', string="Unit of Measure(UoM)", required=True)
    price = fields.Float(string="Price")
    recipe_ids = fields.Many2one('cogs.recipes', string="Recipes Name")
