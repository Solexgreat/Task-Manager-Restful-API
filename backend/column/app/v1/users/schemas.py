import typing as t
from pydantic import BaseModel
from ..custom_base_schemas import CustomBaseModel, CustomIdModel





class UserNoDate(BaseModel):
	email: str
	is_active: bool = True
	is_superuser: bool = True
	last_name: str
	first_name: str
	username: str

class UserBase(CustomBaseModel, UserNoDate):
	pass

class UserCreate(UserNoDate):
	password: t.Optional[str]

	class Config:
		orm_mode = True

class User(UserBase, CustomIdModel):
	pass