from flask import jsonify, request
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config

db = Config.get_database()
collection = db['users']

def signup():
    data = request.get_json()
    # Hash the password before storing it in the database
    data['password'] = generate_password_hash(data['password'])
    result = collection.insert_one(data)
    return jsonify({'message': 'User signed up successfully', 'id': str(result.inserted_id)}), 201

def login():
    data = request.get_json()
    user = collection.find_one({'email': data['email']})
    if user and check_password_hash(user['password'], data['password']):
        user['_id'] = str(user['_id'])
        return jsonify({'message': 'Login successful', 'user': user}), 200
    else:
        return jsonify({'message': 'Invalid email or password'}), 401

def get_all_users():
    users = list(collection.find({}, {'password': 0}))  # Excluding the password field
    for user in users:
        user['_id'] = str(user['_id'])
    return jsonify(users), 200
# Other user-related operations can be added here
# ...
