from . import models as user_model, schemas
from flask import abort



def get_user_by_Id(user_id: str) -> user_model.User:
	"""
		Get user by objectId

	"""
	user = user_model.User.__objects.get(user_id = id)
	if not user:
		raise abort(404, description='User not found')
	return user

def create_user(new_user: schemas.UserCreate) -> user_model.User:
	"""
		Create new user
	"""
	