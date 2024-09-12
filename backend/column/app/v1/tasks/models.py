from mongoengine import Document, StringField, DateTimeField, ReferenceField
import datetime
from ..users.models import User



# Insert a new task
class Tasks(Document):
    title = StringField(requried=True, unique=True)
    description = StringField()
    status = StringField(default='pending')
    due_date = DateTimeField()
    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default= datetime.datetime.now())
    user_id = ReferenceField(User, required=True)