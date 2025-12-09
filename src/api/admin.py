import os
from flask_admin import Admin
from api.database.db import db
from api.models.user import User, OAuthAccount, CustomerProfile
from api.models.recipe import Recipe, Ingredient, RecipeIngredient
from api.models.catalog import Product
from api.models.commerce import CartItem, Order, OrderItem, Payment
from flask_admin.contrib.sqla import ModelView


def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='RECETARIO ADMIN')
    # Dynamically add all models to the admin interface
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(OAuthAccount, db.session))
    admin.add_view(ModelView(CustomerProfile, db.session))
    admin.add_view(ModelView(Recipe, db.session))
    admin.add_view(ModelView(Ingredient, db.session))
    admin.add_view(ModelView(RecipeIngredient, db.session))
    admin.add_view(ModelView(Product, db.session))
    admin.add_view(ModelView(CartItem, db.session))
    admin.add_view(ModelView(Order, db.session))
    admin.add_view(ModelView(OrderItem, db.session))
    admin.add_view(ModelView(Payment, db.session))
