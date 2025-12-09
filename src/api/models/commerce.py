from api.database.db import db
from sqlalchemy import String, Boolean
from datetime import datetime


class CartItem(db.Model):
    __tablename__ = 'cart_item'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), unique=True, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False
    )

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "created_at": self.created_at.isoformat(),
        }


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), nullable=False)
    status = db.Column(String(50), nullable=False)
    subtotal_eur = db.Column(db.Float, nullable=False)
    delivery_fee_eur = db.Column(db.Float, nullable=False)
    total_eur = db.Column(db.Float, nullable=False)
    currency = db.Column(String(10), nullable=False)
    delivery_mode = db.Column(String(50), nullable=False)
    delivery_address = db.Column(String(200), nullable=False)

    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False
    )

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "status": self.status,
            "subtotal_eur": self.subtotal_eur,
            "delivery_fee_eur": self.delivery_fee_eur,
            "total_eur": self.total_eur,
            "currency": self.currency,
            "delivery_mode": self.delivery_mode,
            "delivery_address": self.delivery_address,
            "created_at": self.created_at.isoformat(),
        }


class OrderItem(db.Model):
    __tablename__ = 'order_item'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(
        'order.id'), index=True, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price_eur = db.Column(db.Float, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False
    )

    def serialize(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "created_at": self.created_at.isoformat(),
        }


class Payment(db.Model):
    __tablename__ = 'payment'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(
        'order.id'), unique=True, nullable=False
    )
    provider = db.Column(String(50), nullable=False)
    intent_id = db.Column(String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(String(10), nullable=False)
    status = db.Column(String(50), nullable=False)
    receipt_url = db.Column(String(200), nullable=True)
    creted_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False
    )
    uptdated_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False
    )

    def serialize(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "provider": self.provider,
            "intent_id": self.intent_id,
            "amount": self.amount,
            "currency": self.currency,
            "status": self.status,
            "receipt_url": self.receipt_url,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
