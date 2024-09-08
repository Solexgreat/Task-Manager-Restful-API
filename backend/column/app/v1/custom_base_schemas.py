import datetime
import typing as t
from pydantic import BaseModel, Field
from bson import ObjectId


class PyObjectId(ObjectId):

	@classmethod
	def __get_validators__(cls):

		yield cls.validate

	@classmethod
	def validate(cls, e):
		if not ObjectId.is_valid(e):
			raise ValueError("Invalid Object")
		return ObjectId(e)

	@classmethod
	def __get_pydantic_json_schema__(cls, schema):
			schema.update(type='string')
			return schema

class CustomBaseModel(BaseModel):
	created_at: t.Optional[datetime.datetime]

class CustomIdModel(CustomBaseModel):
	id: t.Optional[PyObjectId]= Field(alias='_id')

	class Config:
		arbitrary_types_allowed = True
		json_encoders = {
			ObjectId : str
		}