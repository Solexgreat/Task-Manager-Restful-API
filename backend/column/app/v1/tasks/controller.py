from . import models as tasks_model
from flask import current_app, abort
from bson import ObjectId
import datetime
from flask_jwt_extended import get_jwt_identity





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

	current_user_id = get_jwt_identity()
	if task.user_id != current_user_id:
		abort(403, description="You do not have permission to modify this task")

	if not task:
		abort(404, description="task not found")

	#Update all the updated field
	updated_field = {f'set__{key}': value for key, value in data.items()}

	#Update the updated_at field
	updated_field['updated_at']= datetime.datetime.now()

	#Check if due_date id present then update the task
	if 'due_date' in data:
		updated_field['due_date'] = data.get('due_date')

	#perform the update
	task.update(**updated_field)

	task.reload()

	return task