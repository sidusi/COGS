{
    "name":"COGS",
    "version":"1.0",
    "website":"",
    "author":"sidusi",
    "description":"""
        Cost Of Good Sold
    """,
    "category":"Sales",
    "depends":["base"],
    "data":[
        'security/ir.model.access.csv',
        'views/recipes.xml',
        'views/ingredients.xml',
        'views/ingredients_categories.xml',
        'views/ingredients_uom.xml',
        'views/menu_items.xml',
    ],
    # the different of data files and demo files is, for the demo files you must check the checkbox Demo data from initial instalation first
    # before it store to the model
    "demos":[
        'demo/property_tag.xml'
    ],
    'assets':{

    },
    "installable":True,
    "application":True,
    "license":"LGPL-3",
}