from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from column.app.v1.users.models import User
from column.app.v1.users.schemas import UserCreate
from column.app.v1.users.controller import create_user
from werkzeug.exceptions import BadRequest, InternalServerError
from bson import ObjectId


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
	return jsonify(created_user.dict())
  # result = db.users.insert_one({"name": names.get_full_name()})
  # return str(result.inserted_id)

@app.route("/list")
def get_user():
		user = db.users.find_one({"name": "Nilda Duffie"})
		if user:
			users= dumps(user)
			return (users)
		else:
			return "User not find"

?
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