from flask import jsonify, request
from bson import ObjectId
from config import Config

db = Config.get_database()
collection = db['jewellery']

def index():
    return jsonify({"message":"success"})

def create_jewellery():
    data = request.get_json()
    result = collection.insert_one(data)
    return jsonify({'message': 'jewellery created successfully', 'id': str(result.inserted_id)}), 201

def get_all_jewellery():
    jewellery = list(collection.find())
    for jwel in jewellery:
        jwel['_id'] = str(jwel['_id'])
    return jsonify(jewellery), 200

def get_jewellery(id):
    jwel = collection.find_one({'_id': ObjectId(id)})
    if jwel:
        jwel['_id'] = str(jwel['_id'])
        return jsonify(jwel), 200
    else:
        return jsonify({'message': 'jewellery not found'}), 404

def update_jewellery(id):
    data = request.get_json()
    result = collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    if result.modified_count == 1:
        return jsonify({'message': 'jewellery updated successfully'}), 200
    else:
        return jsonify({'message': 'jewellery not found'}), 404


def delete_jewellery(id):
    result = collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 1:
        return jsonify({'message': 'jewellery deleted successfully'}), 200
    else:
        return jsonify({'message': 'jewellery not found'}), 404
