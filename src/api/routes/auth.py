from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from flask import Flask, request, jsonify, Blueprint
from api.database.db import db
from api.models.user import User, CustomerProfile, OAuthAccount
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from datetime import datetime, timedelta, timezone
import os
import secrets

# Google OAuth libraries
from google.auth.transport import requests as google_requests
from google.oauth2 import id_token

api = Blueprint('auth', __name__)


@api.route('/register', methods=['POST'])
def register():

    data = request.get_json()

    if not data or not data.get('email') or not data.get('password') or not data.get('role'):
        return jsonify({"message": "Email and password are required"}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "User already exists"}), 400

    new_user = User(
        email=data['email'],
        role=data['role']
    )

    new_user.set_password(data['password'])

    try:
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            "message": "User registered successfully"
        }), 201

    except Exception as e:
        return jsonify({"message": "Error creating user", "error": str(e)}), 500


@api.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"message": "Email and password are required"}), 400
    user = User.query.filter_by(email=data['email']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({"message": "Invalid email or password"}), 401
    access_token = create_access_token(
        identity=str(user.id), expires_delta=timedelta(hours=1))
    return jsonify({
        "access_token": access_token,
        "user": user.serialize()
    }), 200


@api.route('/google', methods=['POST'])
def google_auth():
    """
    Endpoint para autenticarse con Google.
    Espera un token de Google en el body como:
    {
        "token": "google_id_token"
    }
    """
    data = request.get_json()

    if not data or not data.get('token'):
        return jsonify({"message": "Google token is required"}), 400

    try:
        # Verify the Google token
        google_client_id = os.getenv('GOOGLE_CLIENT_ID')
        if not google_client_id:
            return jsonify({"message": "Google Client ID not configured"}), 500

        # Verify the token with Google's OAuth2
        idinfo = id_token.verify_oauth2_token(
            data['token'], google_requests.Request(), google_client_id)

        # Get user info from token
        email = idinfo.get('email')
        name = idinfo.get('name')
        google_id = idinfo.get('sub')

        if not email:
            return jsonify({"message": "Email not provided by Google"}), 400

        # Search for existing user
        user = User.query.filter_by(email=email).first()

        if not user:
            # Create new user if not exists
            user = User(
                email=email,
                role='customer'
            )
            # Generate a random password since Google handles authentication
            user.set_password(secrets.token_urlsafe(32))

            db.session.add(user)
            db.session.commit()

        # Create or update OAuthAccount
        oauth_account = OAuthAccount.query.filter_by(
            provider='google',
            provider_user_id=google_id
        ).first()

        if not oauth_account:
            oauth_account = OAuthAccount(
                provider='google',
                provider_user_id=google_id,
                user_id=user.id
            )
            db.session.add(oauth_account)
            db.session.commit()

        # Create token
        access_token = create_access_token(
            identity=str(user.id), expires_delta=timedelta(hours=1))

        return jsonify({
            "message": "User authenticated with Google",
            "access_token": access_token,
            "user": user.serialize()
        }), 200

    except ValueError as e:
        # Invalid token
        return jsonify({"message": "Invalid Google token", "error": str(e)}), 401
    except Exception as e:
        return jsonify({"message": "Error authenticating with Google", "error": str(e)}), 500
