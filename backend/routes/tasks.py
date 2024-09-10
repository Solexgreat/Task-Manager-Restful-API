from flask import request, jsonify
from . import task_bp
from ..column.app.v1.tasks.controller import create_task
from werkzeug.exceptions import BadRequest


@task_bp.route("/create_task", methods=['POST'])
def create__task():
	try:
		data = request.json
		task_id= create_task(data)
		return jsonify({"task_id": task_id}), 201
	except BadRequest as e:
		return jsonify({"error": str(e)}), 400
	except Exception as e:
		return jsonify({"error": str(e)}), 500