from . import models as user_model, schemas
from flask import abort
from ..core.security import get_hashed_password



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
	new_user_dict = new_user.model_dump(exclude_unset=True)
	if "password" in new_user_dict and new_user_dict["password"]:
		hashed_password = get_hashed_password(new_user_dict["password"])
		new_user_dict["password"] = hashed_password
	saved_user = user_model.User(**new_user_dict).save()
	return new_user