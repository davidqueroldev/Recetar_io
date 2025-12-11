from api.database.db import db
from sqlalchemy import String, Boolean
from datetime import datetime


class CalendarEntry(db.Model):
    __tablename__ = 'calendar_entry'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # e.g., breakfast, lunch, dinner
    meal_type = db.Column(String(50), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey(
        'recipe.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'meal_type': self.meal_type,
            'recipe_id': self.recipe_id,
        }


class PantryItem(db.Model):
    __tablename__ = 'pantry_item'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey(
        'ingredient.id'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'ingredient_id': self.ingredient_id,
            'quantity': self.quantity,
            'updated_at': self.updated_at.isoformat(),
        }
