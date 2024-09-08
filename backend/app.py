from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from column.app.v1.users.models import User
from column.app.v1.users.schemas import UserCreate
from column.app.v1.users.controller import create_user, get_user_by_Id
from werkzeug.exceptions import BadRequest, InternalServerError
from bson import ObjectId
from column.app.v1.custom_base_schemas import PyObjectId


app = Flask(__name__)
client = MongoClient("mongodb+srv://Solexgreat:solexgreat1$@cluster0.wekq3.mongodb.net/")
db = client.flask_example_db


@app.route('/')
def index():
	return "Hello, Flask with mongodb"

@app.route("/create-user", methods=["POST"])
def add_user():
	data= request.json
	if not data:
		raise BadRequest("Invalid or missing JSON data")

	new_user = UserCreate(**data)
	if User.objects(email=new_user.email).first():
		raise BadRequest(f"User with email {new_user.email} already exist")

	created_user = create_user(new_user)
	user_dict = created_user.to_mongo().to_dict()
	user_dict['_id'] = str(user_dict['_id'])
	return jsonify(user_dict)

@app.route("/user/<user_id>", methods=['GET'])
def get_user(user_id):
	obj_id = PyObjectId.validate(user_id)
	user2 = db.user.find_one({'_id': obj_id})
	user1 = get_user_by_Id(obj_id)
	user_dict = user1.to_mongo().to_dict()
	user_dict['_id'] = str(user_dict['_id'])
	return jsonify(user_dict, user2)
	# users =  list(db.user.find({}))
	# if users:
	# 	return dumps(users)
	# else:
	# 	return "User not find"



# @app.route('/tasks', methods=['POST'])
# def create_task():
# 	data = request.get_json()
# 	user = User.Objects(id=data[user.id])
# 	if user is None:
# 		return jsonify({'Error': 'user not found'}), 404

# 	task = Task(
# 		title = data['title'],
# 		description = data.get('description', ''),
# 		status = data.get('status', 'pending'),
# 		user_id = user,
# 	)
# 	return jsonify({'_id': str(task.id)}), 201



if __name__ == '__main__':
	app.run(debug=True)