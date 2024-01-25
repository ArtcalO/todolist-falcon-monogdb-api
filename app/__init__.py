import falcon
import mongoengine as mongo
from app.settings import middleware,dbcfg
app = falcon.API(middleware=middleware)
db = mongo.connect(
    'todolist', # This will be the name of your database
    host=dbcfg['host'],
    port=dbcfg['port'],
)

from app.ressources.TaskRessource import *
app.add_route('/tasks/', GetTask)