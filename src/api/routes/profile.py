from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from flask import Flask, request, jsonify, Blueprint
from api.database.db import db
from api.models.user import User, CustomerProfile, OAuthAccount
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from datetime import datetime, timedelta, timezone
import os
import secrets

api = Blueprint('me', __name__)

# Profile route to create or update customer profile


@api.route('/profile', methods=['POST'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"message": "No data provided"}), 400

    try:
        # Search for existing customer profile
        customer_profile = CustomerProfile.query.filter_by(
            user_id=user_id).first()

        if not customer_profile:
            # Create a new profile if it doesn't exist
            customer_profile = CustomerProfile(user_id=user_id)

        # Update fields if they exist in the request
        if 'height_cm' in data:
            customer_profile.height_cm = data['height_cm']
        if 'weight_kg' in data:
            customer_profile.weight_kg = data['weight_kg']
        if 'age' in data:
            customer_profile.age = data['age']
        if 'diet_type' in data:
            customer_profile.diet_type = data['diet_type']
        if 'meals_per_day' in data:
            customer_profile.meals_per_day = data['meals_per_day']
        if 'preferences' in data:
            customer_profile.preferences = data['preferences']
        if 'adress' in data:
            customer_profile.adress = data['adress']

        db.session.add(customer_profile)
        db.session.commit()

        return jsonify({
            "message": "Profile updated successfully",
            "user": user.serialize()
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error updating profile", "error": str(e)}), 500
