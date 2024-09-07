from mongoengine import Document, StringField, DateTimeField, ReferenceField
import datetime
from ..users.models import User



# Insert a new task
class Task(Document):
    title = StringField(requried=True, unique=True)
    description = StringField()
    status = StringField(default='pending')
    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=lambda: datetime.datetime.now(datetime.timezone.utc))
    user_id = ReferenceField(User, required=True)