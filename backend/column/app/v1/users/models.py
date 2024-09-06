from mongoengine import Document, StringField, DateTimeField, ReferenceField
import datetime


# Insert a new user
class User(Document):
    username = StringField(requried=True, unique=True)
    email = StringField(requried=True, unique=True)
    password_hash = StringField(requried=True)
    created_at = DateTimeField(default=datetime.datetime.utcnow())
    updated_at = DateTimeField(default=lambda: datetime.datetime.now(datetime.timezone.utcnow()))
