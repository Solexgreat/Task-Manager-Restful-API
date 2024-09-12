from flask import jsonify, request, Flask, current_app
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from . import auth_bp
from ..column.app.v1.core.auth import login_user


@auth_bp.route("/login", methods=['POST'])
def login():
	data = request.json

	if not data or not data.get('username') or not data.get('password'):
		return jsonify({'msg':'Missing username or password'}), 400

	username = data['username']
	password = data['password']


	result = login_user(username, password)
	if result:
		user = current_app.db.user.find_one({'username': username})
		access_token = create_access_token(identity=str(user['_id']))
		return jsonify(access_token=access_token), 200
	else:
		return jsonify({"msg": "Bad credentials"}), 401
