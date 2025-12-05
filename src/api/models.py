from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(String(120), unique=True, nullable=False)
    password = db.Column(String(128), nullable=False)
    name = db.Column(String(120), nullable=False)
    last_name = db.Column(String(120), nullable=True)
    height_cm = db.Column(db.Float, nullable=True)
    weight_kg = db.Column(db.Float, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    diet_type = db.Column(String(50), nullable=True)
    role = db.Column(String(50), nullable=False)
    is_active = db.Column(Boolean(), default=True, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)

    oauth_accounts = db.relationship(
        "OAuthAccount",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    customer = db.relationship(
        "Customer", back_populates="user", cascade="all, delete-orphan")
    seller = db.relationship(
        "Seller", back_populates="user", cascade="all, delete-orphan")
    distributor = db.relationship("Distributor", back_populates="user",
                                  cascade="all, delete-orphan")
    img_url = db.relationship(
        "ImgUrl", back_populates="user", cascade="all")
    recipe = db.relationship("Recipe", back_populates="user",
                             cascade="all")
    payment = db.relationship("Payment", back_populates="user",
                              cascade="all")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class OAuthAccount(db.Model):
    __tablename__ = 'oauth_account'
    id = db.Column(db.Integer, primary_key=True)
    seller = db.Column(String(50), nullable=False)
    seller_user_id = db.Column(String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)

    user = db.relationship("User", back_populates="oauth_accounts")

    def serialize(self):
        return {
            "id": self.id,
            "seller": self.seller,
            "seller_user_id": self.seller_user_id,
            "user_id": self.user_id,
        }


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(String(100), nullable=False)
    address = db.Column(String(200), nullable=False)
    phone_number = db.Column(String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)

    user = db.relationship("User", back_populates="customer")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone_number": self.phone_number,
        }


class Seller(db.Model):
    __tablename__ = 'seller'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(String(100), nullable=False)
    service_type = db.Column(String(100), nullable=False)
    contact_email = db.Column(String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)

    user = db.relationship("User", back_populates="seller")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "service_type": self.service_type,
            "contact_email": self.contact_email,
        }


class Distributor(db.Model):
    __tablename__ = 'distributor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(String(100), nullable=False)
    vehicle_type = db.Column(String(100), nullable=False)
    license_number = db.Column(String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)

    user = db.relationship("User", back_populates="distributor")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "vehicle_type": self.vehicle_type,
            "license_number": self.license_number,
        }


class ImgUrl(db.Model):
    __tablename__ = 'img_url'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(String(500), nullable=False)
    description = db.Column(String(200), nullable=True)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    user = db.relationship("User", back_populates="img_url")

    recipe_id = db.Column(
        db.Integer, db.ForeignKey('recipe.id'), nullable=True)

    recipe = db.relationship("Recipe", back_populates="img_url")

    def serialize(self):
        return {
            "id": self.id,
            "url": self.url,
            "description": self.description,
        }


class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(String(200), nullable=False)
    description = db.Column(String(500), nullable=True)
    instructions = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship("User", back_populates="recipe")
    img_url = db.relationship("ImgUrl", back_populates="recipe",
                              cascade="all")

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "instructions": self.instructions,
        }


class Payment(db.Model):
    __tablename__ = 'payment'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(String(10), nullable=False)
    payment_date = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship("User", back_populates="payment")

    def serialize(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "currency": self.currency,
            "payment_date": self.payment_date.isoformat(),
        }
