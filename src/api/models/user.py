from api.database.db import db
from sqlalchemy import String, Boolean
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(String(120), unique=True, nullable=False)
    password = db.Column(String(128), nullable=False)
    role = db.Column(String(50), nullable=False)
    is_active = db.Column(Boolean(), default=True, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)

    oauth_accounts = db.relationship(
        "OAuthAccount",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    customer_profiles = db.relationship(
        "CustomerProfile", back_populates="user",
        cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class OAuthAccount(db.Model):
    __tablename__ = 'oauth_account'
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(String(50), unique=True, nullable=False)
    provider_user_id = db.Column(String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)

    user = db.relationship("User", back_populates="oauth_accounts")

    def serialize(self):
        return {
            "id": self.id,
            "provider": self.provider,
            "provider_user_id": self.provider_user_id,
            "user_id": self.user_id,
        }


class CustomerProfile(db.Model):
    __tablename__ = 'customer_profile'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    height_cm = db.Column(db.Float, nullable=True)
    weight_kg = db.Column(db.Float, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    diet_type = db.Column(String(50), nullable=True)
    meals_per_day = db.Column(db.Integer, nullable=True)
    preferences = db.Column(String(250), nullable=True)
    adress = db.Column(String(250), nullable=True)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)

    user = db.relationship("User", back_populates="customer_profiles")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "height_cm": self.height_cm,
            "weight_kg": self.weight_kg,
            "age": self.age,
            "diet_type": self.diet_type,
            "meals_per_day": self.meals_per_day,
            "preferences": self.preferences,
            "adress": self.adress,
        }
