import falcon
import mongoengine as mongo
from app.settings import middleware,dbcfg
from app.docs.ApiDocs import *

app = falcon.App(middleware=middleware)
db = mongo.connect(
    'todolist', # This will be the name of your database
    host=dbcfg['host'],
    port=dbcfg['port'],
)

from app.ressources.TaskRessource import *
task = Task()
app.add_route('/tasks/{id}', task)
app.add_route('/tasks', task)
app.add_route('/tasks', task, suffix='collection')

spec.register(app)