from flask import request, jsonify, current_app,json
from . import task_bp
from ..column.app.v1.tasks.controller import create_task, get_task, update_task
from werkzeug.exceptions import BadRequest
from ..column.app.v1.custom_base_schemas import PyObjectId
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from bson import json_util


@task_bp.route("/create_task", methods=['POST'])
@jwt_required()
def create__task():
	try:
		data = request.json
		task_id= create_task(data)
		return jsonify({"task_id": task_id}), 201
	except BadRequest as e:
		return jsonify({"error": str(e)}), 400
	except Exception as e:
		return jsonify({"error": str(e)}), 500

@task_bp.route("/get_task/<identifier>", methods=['GET'])
def get__task(identifier):
	obj_id = PyObjectId.validate(identifier)
	try:
		task = get_task(obj_id)
		return jsonify(task), 200
		# task = list(current_app.db.tasks.find({'user_id': obj_id}))
		# return jsonify(json.loads(json_util.dumps(task)))
	except BadRequest as e:
		return jsonify({"error": str(e)}), 400
	except Exception as e:
		return jsonify ({"error": str(e)}), 500

@task_bp.route("/update_task/<task_id>", methods=['PUT'])
@jwt_required()
def update__task(task_id):
	data = request.json
	try:
		task = update_task(task_id, data)
		task_dict = task.to_mongo().to_dict()
		task_dict['_id']= str(task_dict['_id'])
		task_dict['user_id'] = str(task_dict['user_id'])
		return jsonify(task_dict), 200
	except BadRequest as e:
		return jsonify({"error": str(e)}), 404
	except Exception as e:
		return jsonify({'error': str(e)}), 500

@task_bp.route("/delete/<task_id>", methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
	"""
	    Delete a specific task
	"""
	try:
		obj_id = PyObjectId.validate(task_id)
		task = current_app.db.tasks.delete_one({'id': obj_id})
		if task:
			return jsonify({"message": "Task delete Successfully"}), 200
		else:
			raise BadRequest("Invalid request")
	except BadRequest as e:
		return jsonify ({"error": str(e)}), 404
	except Exception as e:
		return jsonify ({"error": str(e)}), 500
