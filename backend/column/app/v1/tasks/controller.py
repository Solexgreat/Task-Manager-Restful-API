from . import models as tasks_model
from flask import current_app, abort
from bson import ObjectId




def create_task(data: dict)-> tasks_model.Tasks:
	"""
			Create a Task
	"""
	user_id = data.get('user_id')
	if not ObjectId.is_valid(user_id):
		abort(400, description="Invalid user_id format")

	user = current_app.db.user.find_one({'_id': ObjectId(data['user_id'])})
	if not user:
		raise abort(404, description="user not found")
	task = tasks_model.Tasks(**data).save()
	task_dict = task.to_mongo().to_dict()
	return str(task_dict['_id'])