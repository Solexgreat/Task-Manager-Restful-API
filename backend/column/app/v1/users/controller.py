from . import models as user_model, schemas
from flask import abort
from ..core.security import get_hashed_password
from bson import ObjectId
import datetime


def get_user_by_Id(user_id: str) -> user_model.User:
	"""
		Get user by objectId

	"""
	user = user_model.User.objects.get(id = ObjectId(user_id))
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
		new_user_dict["password_hash"] = hashed_password
		new_user_dict.pop("password")
	saved_user = user_model.User(**new_user_dict).save()
	return saved_user

def get_user_by_email(user_email: str)-> user_model.User:
	"""
			Get user by email
	"""
	try:
		user = user_model.User.objects.get(email= user_email)
		return user
	except Exception:
		raise abort(404, description= "user not found")

def update_user_by_id(user_id: ObjectId, data: dict)-> user_model.User:
	"""
			Updating user by Id
	"""
	user = user_model.User.objects(id = user_id).first()
	if not user:
		raise abort(404, description = "user not found")
	user_model.User.objects(id=user_id).update(
		**{f'set__{key}':value for key, value in data.items()},
		set__updated_at=datetime.datetime.now())
	return user