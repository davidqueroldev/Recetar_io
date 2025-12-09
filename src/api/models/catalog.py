from api.database.db import db
from sqlalchemy import String, Boolean
from datetime import datetime


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey(
        'ingredient.id'), nullable=False)
    name = db.Column(String(100), nullable=False)
    brand = db.Column(String(100), nullable=True)
    package_size = db.Column(String(50), nullable=True)
    unit = db.Column(String(20), nullable=True)
    price_eur = db.Column(db.Float, nullable=False)
    storte_name = db.Column(String(100), index=True, nullable=True)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False
    )

    def serialize(self):
        return {
            "id": self.id,
            "ingredient_id": self.ingredient_id,
            "name": self.name,
            "brand": self.brand,
            "package_size": self.package_size,
            "unit": self.unit,
            "price_eur": self.price_eur,
            "store_name": self.storte_name,
            "created_at": self.created_at.isoformat(),
        }
