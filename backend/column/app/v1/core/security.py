# import uuid
import bcrypt


def get_hashed_password(password: str)-> bytes:
	"""
			Convery Password to Hashed format
	"""
	salt = bcrypt.gensalt()
	hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
	return hashed