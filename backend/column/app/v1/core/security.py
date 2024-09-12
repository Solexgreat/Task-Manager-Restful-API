import uuid
import bcrypt
import datetime
from werkzeug.exceptions import BadRequest
from ..users import models as user_model


def get_hashed_password(password: str)-> bytes:
	"""
			Convert input Password to Hashed format
	"""
	salt = bcrypt.gensalt()
	hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
	return hashed.decode('utf-8')

def _generate_uuid():
	"""
			Generate and return
			string uuid
	"""
	return str(uuid.uuid4())

def verify_password(plain_password: str, hashed_password:bytes)-> bool:
	"""
			verify password and return True or False
	"""
	return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

def get_reset_password_token(user_email: str)-> str:
	"""
			Generate new password token
	"""
	#verify user
	user = user_model.User.objects(email=user_email).first()
	if not user:
		raise BadRequest("Invalid User")
	#generate reset_token
	reset_token = _generate_uuid()

	 # Update the user document in the database to include the reset_token
	user.update(set__reset_token= reset_token, set__updated_at= datetime.datetime.now())

	#Reload user to reflect the changes
	user.reload()

	return user.reset_token
	# user = user_model.User.objects(email=user_email).update()

def update_password(reset_token: str, new_password: str)-> None:
	"""
			Update user password if token is available
	"""
	#verify the reste_token
	user = user_model.User.objects(reset_token=reset_token).first()
	if not user:
		raise BadRequest("Inavalid reset_token")
	#convert the password to hashed_password
	hashed_password = str(get_hashed_password(new_password))

	#update the user password
	user.update(set__password_hash=hashed_password, set__updated_at=datetime.datetime.now())
	return None