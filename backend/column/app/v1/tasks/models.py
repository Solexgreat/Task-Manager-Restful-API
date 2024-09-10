from mongoengine import Document, StringField, DateTimeField, ReferenceField, connect
import datetime
from ..users.models import User

connect(db='flask_example_db', alias='default', host='mongodb+srv://Solexgreat:solexgreat1$@cluster0.wekq3.mongodb.net')



# Insert a new task
class Tasks(Document):
    title = StringField(requried=True, unique=True)
    description = StringField()
    status = StringField(default='pending')
    due_date = DateTimeField()
    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default= datetime.datetime.now())
    user_id = ReferenceField(User, required=True)