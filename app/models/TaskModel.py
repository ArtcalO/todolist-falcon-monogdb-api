from mongoengine import *
import datetime

class TaskModel(Document):
   title = StringField(max_length=200, required=True)
   body = StringField(max_length=32, required=True)
   created_at = DateTimeField(default=datetime.datetime.utcnow())