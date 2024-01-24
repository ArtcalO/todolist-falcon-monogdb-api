import falcon
import mongoengine as mongo
from app.settings import middleware
app = falcon.API(middleware=middleware)
db = mongo.connect(
    'todolist', # This will be the name of your database
    host=dbcfg['host'],
    port=dbcfg['port'],
    username=dbcfg['username'],
    password=dbcfg['password']
)