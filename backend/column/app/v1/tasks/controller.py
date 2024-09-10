from . import models as tasks_model
from flask import current_app, abort
from bson import ObjectId
import datetime




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

def get_task(id: ObjectId)-> tasks_model.Tasks:
	"""
			Get and Return task
	"""
	tasks = tasks_model.Tasks.objects(user_id=id)

	#verify task
	if not tasks:
		raise abort(404, description="Task not found")

	task_list= []
	for task in tasks:
		task_list.append({
			'id': str(task.id),
			'title': task.title,
			'description': task.description,
			'status': task.status,
			'created_at': task.created_at,
			'updated_at': task.updated_at,
			'user_id': str(task.user_id.id)
	})

	return task_list

def update_task(task_id: str, data: dict)-> tasks_model.Tasks:
	"""
			Upddate and return the updated task
	"""
	task = tasks_model.Tasks.objects(id=task_id).first()
	if not task:
		raise abort(404, description="task not found")

	tasks_model.Tasks.objects(id=task_id).update(
		**{f'set__{key}': value for key, value in data.items()},
			set__updated_at = datetime.datetime.now()
		})

	return task