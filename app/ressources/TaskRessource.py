import falcon
from app import db
from app.models.TaskModel import TaskModel
class Task:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        tasks = []
        tasks_obj = TaskModel.objects
        for obj in tasks_obj:
            tasks.append(obj)

        resp.context.result = tasks

    def on_post(self, req, resp):
        data = req.context.doc
        title = data['title']
        body = data["body"]

        task_obj = TaskModel(
            title=title, body=body
        )


        task_obj.save()

        resp.status = falcon.HTTP_201
        resp.context.result = "created"