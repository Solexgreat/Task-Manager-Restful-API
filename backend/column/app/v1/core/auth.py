from flask import Flask, abort
from ..users import models as user_model
from .security import verify_password
# import bcrypt


def login_user(username:str, password:str)-> bool:
	"""
			Login user if the details are correct
	"""
	#get user and verify the user
	user = user_model.User.objects(username=username).first()
	if not user:
		raise abort(404, description="Invalid Username")

	#Get the user password and verify the password
	stored_hashed_password = user['password_hash']
	hashed_password = stored_hashed_password.encode('utf-8')

	if not verify_password(password, hashed_password):
		raise abort(404, description="Invalid password")

	return True
