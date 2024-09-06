import datetime
import typing as t
from pydantic import BaseModel, Field
from bson import ObjectId


class PyObjectId(ObjectId):

	@classmethod
	def __get__validators__(cls):

		yield cls.validate

	@classmethod
	def validate(cls, e):
		if not ObjectId.is_valid(e):
			raise ValueError("Invalid Object")
		return ObjectId(e)

	@classmethod
	def __modify_schema__(cls, field_schema):
		field_schema.update(type='string')

class CustomBaseModel(BaseModel):
	created_at: t.Optional[datetime.datetime]

class CustomIdModel(CustomBaseModel):
	id: t.Optional[PyObjectId]= Field(alias='_id')

	class config:
		arbitrary_types_allowed = True
		json_encoder = {
			ObjectId : str
		}