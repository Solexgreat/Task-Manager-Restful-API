from mongoengine import Document, StringField, DateTimeField, ReferenceField
import datetime


# Insert a new user
class User(Document):
    username = StringField(requried=True, unique=True)
    email = StringField(requried=True, unique=True)
    password_hash = StringField(requried=True)
    created_at = DateTimeField(default=datetime.datetime.utcnow())
    updated_at = DateTimeField(default=lambda: datetime.datetime.now(datetime.timezone.utc))

# Insert a new task
class Task(Document):
    title = StringField(requried=True, unique=True)
    description = StringField()
    status = StringField(default='pending')
    created_at = DateTimeField(default=datetime.datetime.utcnow())
    updated_at = DateTimeField(default=lambda: datetime.datetime.now(datetime.timezone.utc))
    user_id = ReferenceField(User, required=True)
