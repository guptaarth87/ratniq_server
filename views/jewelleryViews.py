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

def filter_jewellery():
    query = {}
    filter_data = request.get_json()

    if 'gender' in filter_data:
        query['gender'] = {'$in': filter_data['gender']}
    if 'metal' in filter_data:
        query['metal'] = {'$in': filter_data['metal']}
    if 'price' in filter_data:
        query['price'] = {'$lte': filter_data['price']}
    if 'jewellery_type' in filter_data:
        query['jewellery_type'] = filter_data['jewellery_type']
    if 'color_theme' in filter_data:
        query['color_theme'] = {'$in': filter_data['color_theme']}
    if 'vendor' in filter_data:
        query['vendor'] = filter_data['vendor']
    if 'city' in filter_data:
        query['city'] = filter_data['city']

    result = list(collection.find(query, {'_id': 0}))
    return jsonify(result), 200

# sample schema
# {
#    "jewellery_image" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKDEFKY1tiFizHIBxiayHsRaFXb8ip3u6DkA&usqp=CAU",
#    "occassions" : ["wedding" , "traditional"],
#    "gender" : ["F"] ,
#    "metal" : ["gold" , "diamond"] ,
#    "price" : 95000,
#    "jewellery_type" : "ring" , 
#    "color_theme" : [] ,
#    "vendor" : "jmc jewellers",
#    "city" : "Indore" 
 
# }