import falcon
from app import db
from app.models.TaskModel import TaskModel
import json
class Task:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        tasks = []
        tasks_obj = TaskModel.objects
        for obj in tasks_obj:
            tasks.append(obj.to_mongo())

        resp.context.result = tasks[0]

    def on_post(self, req, resp):
        data = req.context.doc
        title = data['title']
        body = data["body"]

        task_obj = TaskModel(
            title=title, body=body
        )

        task_obj.save()

        resp.status = falcon.HTTP_201
        resp.context.result = task_obj