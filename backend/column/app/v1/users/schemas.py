import typing as t
from pydantic import BaseModel





class UserNoDate(BaseModel):
	email: str
	is_active: bool = True
	is_superuser: bool = True
	last_name: str
	first_name: str
	username: str

class 