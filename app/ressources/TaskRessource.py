import falcon
from app import db
from app.models.TaskModel import TaskModel
class GetTask(object):
    def on_get(self, req, resp, id):
        resp.status = falcon.HTTP_200
        tasks = []
        tasks_obj = TaskModel.objects.all()
        for obj in tasks_obj:
            tasks.append(obj)
        resp.json = {
            'tasks': tasks
        }
        
    def on_post(self, req, resp):
        title = resp.get_json('title', dtype=str)
        body = resp.get_json('body', dtype=str)
        task_obj = TaskModel(
            title=title, body=body
        )
        task_obj.save()

        resp.status = falcon.HTTP_201
        resp.json = {
            'message': 'Your task has been registered',
            'status': 200,
            'successful': True
        }