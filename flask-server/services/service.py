import datetime
from dotenv import load_dotenv
import re
import uuid
from flask import request, jsonify, session
from flask_jwt_extended import create_access_token
import jwt
from models.model import  MongoDB
import hashlib
import os
from hashlib import sha256
from flask import session
from pymongo import MongoClient
from  faker import Faker


load_dotenv()
mongo_uri = os.getenv('MONGO_URI')
client = MongoClient(mongo_uri)
db = client ['ShoppingCart']
collection = db['products']



class Service:
    
    
    def __init__(self):
        self.mongodb = MongoDB()
        self.fake = Faker()

    def register(self):
        data = request.get_json()
        email = data['email']
        username = data['username']
        password = data['password']

        # Check username requirements
        if len(username) < 8:
            return jsonify({'message': 'Username must be at least 8 characters long'})

        # Check password requirements
        if not re.search(r'[A-Z]', password) or \
        not re.search(r'[a-z]', password) or \
        not re.search(r'[!@#$%^&*(),.?":{}|<>]', password) or \
        len(password) < 8:
            return jsonify({'message': 'Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one special character, and one digit'})

        # Check if username already exists
        if self.mongodb.clientusers.find_one({'username': username}) is not None:
            return jsonify({'message': 'Username already exists'})

        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user_id = str(uuid.uuid4())
        user = {
            '_id': user_id,
            'username': username,
            'password': hashed_password,
            'email':email
        }
        self.mongodb.clientusers.insert_one(user)
        return jsonify({'user_id':user_id,'message': 'User created successfully'})
    
    def login(self):
        data = request.get_json()
        email =data['email']
        username = data['username']
        password = data['password']
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user = self.mongodb.clientusers.find_one({'username': username})
        if user and email==user['email'] and user['password'] == hashed_password:
            # Create access token
            access_token = create_access_token(identity=str(user['_id']))
            return jsonify({'user_id':str(user['_id']),'access_token': access_token})
        else:
            return jsonify({'message': 'Invalid username or password or email'})
    
    