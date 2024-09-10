from flask import  request, jsonify, current_app
from ..column.app.v1.users.controller import create_user, get_user_by_Id, get_user_by_email, update_user_by_id
from ..column.app.v1.core.security import get_reset_password_token, update_password
from werkzeug.exceptions import BadRequest
from ..column.app.v1.users.models import User
from ..column.app.v1.users.schemas import UserCreate
from bson import ObjectId, json_util
from bson.json_util import dumps
from ..column.app.v1.custom_base_schemas import PyObjectId
from . import user_bp



@user_bp.route('/')
def index():
	return "Hello, Flask with mongodb"

@user_bp.route("/create-user", methods=["POST"])
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

@user_bp.route("/id/<user_id>", methods=['GET'])
def get_user(user_id):
	obj_id = PyObjectId.validate(user_id)
	# user2 = db.user.find_one({'_id': obj_id})
	user = get_user_by_Id(obj_id)
	if user:
		user_dict = user.to_mongo().to_dict()
		user_dict['_id'] = str(user_dict['_id'])
		return jsonify(user_dict)
	else:
		return jsonify({"error": "user not found"})
	# return jsonify(json.loads(json_util.dumps(user2)))

@user_bp.route("/email/<email_id>", methods=['GET'])
def user_by_email(email_id):
	user = get_user_by_email(email_id)
	if user:
		user_dict = user.to_mongo().to_dict()
		user_dict['_id'] = str(user_dict['_id'])
		return jsonify(user_dict)
	else:
		return jsonify({"error": "user not found"})

@user_bp.route("/update/<user_id>", methods=['PUT'])
def update_user(user_id):
	"""
	"""
	data = request.json
	obj_id = PyObjectId.validate(user_id)
	updated_user = update_user_by_id(obj_id, data)
	user_dict = updated_user.to_mongo().to_dict()
	user_dict['_id'] = str(user_dict['_id'])
	return jsonify(user_dict)
	# Pymongo Methods
	# result = db.user.update_one({'_id': obj_id},{'$set':
	# 																						{**data, 'updated_at': datetime.datetime.now()}})
	# 	return jsonify({"error": "user not found"})
	# user = db.user.find_one({"_id": obj_id})
	# return jsonify (json.loads(json_util.dumps(user)))

@user_bp.route("/reset_tokens/<user_email>", methods=['GET'], strict_slashes=False)
def reset_token(user_email):
	try:
		reset_token = get_reset_password_token(user_email)
		return jsonify({"reset_token": reset_token}), 200
	except BadRequest as e:
			return jsonify({"error": str(e)}), 400
	except Exception as e:
			return jsonify({"error": "An error occurred"}), 500

@user_bp.route("/reset_password", methods=['POST'], strict_slashes=False)
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
