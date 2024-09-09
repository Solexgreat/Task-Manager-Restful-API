from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from column.app.v1.users.models import User
from column.app.v1.users.schemas import UserCreate
from column.app.v1.users.controller import create_user, get_user_by_Id, get_user_by_email, update_user_by_id
from column.app.v1.core.security import get_reset_password_token, update_password
from werkzeug.exceptions import BadRequest, InternalServerError
from bson import ObjectId, json_util
from column.app.v1.custom_base_schemas import PyObjectId
import json
import datetime


app = Flask(__name__)
client = MongoClient("mongodb+srv://Solexgreat:solexgreat1$@cluster0.wekq3.mongodb.net/")
db = client.flask_example_db




@app.route("/reset_tokens/<user_email>", methods=['GET'], strict_slashes=False)
def reset_token(user_email):
	try:
		reset_token = get_reset_password_token(user_email)
		return jsonify({"reset_token": reset_token}), 200
	except BadRequest as e:
			return jsonify({"error": str(e)}), 400
	except Exception as e:
			return jsonify({"error": "An error occurred"}), 500

@app.route("/reset_password", methods=['POST'], strict_slashes=False)
def reset_password():
	data = request.json
	try:
		updated_password= update_password(data['reset_token'], data['password'])
		if updated_password is None:
			return jsonify({"success": "password changed successfully"}), 200
	except BadRequest as e:
		return jsonify({'error': str(e)}), 400
	except Exception as e:
		return jsonify({"error": str(e)}), 500


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