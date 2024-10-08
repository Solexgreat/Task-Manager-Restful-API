from mongoengine import Document, StringField, DateTimeField, BooleanField
import datetime




# Insert a new user
class User(Document):
    username = StringField(max_length=200, requried=True, unique=True)
    email = StringField(max_length=100, requried=True, unique=True)
    last_name = StringField(max_length= 200)
    first_name = StringField(max_length= 200)
    is_active = BooleanField(required=True, default=True)
    is_superuser = BooleanField(required=True, default=True)
    reset_token = StringField()
    password_hash = StringField(requried=True)
    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())
