from flask import Flask
from flask_cors import CORS
import os
from views.jewelleryViews import create_jewellery, get_all_jewellery , index , get_jewellery,update_jewellery,delete_jewellery, filter_jewellery
from views.usersViews import signup, login , get_all_users
# Import other CRUD operations from views as needed

app = Flask(__name__)
CORS(app)

# Routes
app.add_url_rule('/','serve_html_page' , index )
app.add_url_rule('/jewellery', 'create_jewellery', create_jewellery, methods=['POST'])
app.add_url_rule('/jewellery', 'get_all_jewellery', get_all_jewellery, methods=['GET'])
app.add_url_rule('/jewellery/<id>', 'get_jewellery', get_jewellery, methods=['GET'])
app.add_url_rule('/jewellery/<id>', 'update_jewellery', update_jewellery, methods=['PUT'])
app.add_url_rule('/jewellery/<id>', 'delete_jewellery', delete_jewellery, methods=['DELETE'])

app.add_url_rule('/filterjewellery', 'filter_jewellery', filter_jewellery , methods=['POST'])

# users
app.add_url_rule('/signup', 'signup', signup, methods=['POST'])
app.add_url_rule('/login', 'login', login, methods=['POST'])
app.add_url_rule('/users', 'get_all_users', get_all_users, methods=['GET'])  # New route for getting all users

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
