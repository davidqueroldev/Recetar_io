from api.database.db import db
from sqlalchemy import String, Boolean
from datetime import datetime


class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(String(200), nullable=False, index=True)
    description = db.Column(db.String(1000), nullable=True)
    instructions = db.Column(db.String(2000), nullable=False)
    total_time_minutes = db.Column(db.Integer, nullable=True)
    difficulty = db.Column(String(50), nullable=True)
    diet_tags = db.Column(String(200), nullable=True)  # Comma-separated tags
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "tittle": self.tittle,
            "description": self.description,
            "instructions": self.instructions,
            "total_time_minutes": self.total_time_minutes,
            "difficulty": self.difficulty,
            "diet_tags": self.diet_tags.split(",") if self.diet_tags else [],
            "created_at": self.created_at.isoformat(),
        }


class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(String(100), unique=True, nullable=False, index=True)
    default_unit = db.Column(String(20), nullable=False)
    category = db.Column(String(50), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "default_unit": self.default_unit,
            "category": self.category,
        }


class RecipeIngredient(db.Model):
    __tablename__ = 'recipe_ingredient'
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey(
        'recipe.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey(
        'ingredient.id'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit = db.Column(String(20), nullable=False)

    recipe = db.relationship("Recipe", backref=db.backref(
        "recipe_ingredients", cascade="all, delete-orphan"))
    ingredient = db.relationship("Ingredient", backref=db.backref(
        "recipe_ingredients", cascade="all, delete-orphan"))

    def serialize(self):
        return {
            "id": self.id,
            "recipe_id": self.recipe_id,
            "ingredient_id": self.ingredient_id,
            "quantity": self.quantity,
            "unit": self.unit,
        }
