import falcon
from app import db
from app.models.TaskModel import TaskModel
from bson import ObjectId
import json
from app.docs.ApiDocs import *
from spectree import  Response

class Task:

    def on_get(self, req, resp, id):
        try:
            task_obj = TaskModel.objects(id=id)

            resp.status = falcon.HTTP_200
            resp.context.result = task_obj[0].to_mongo()
        except Exception as e:
            raise falcon.HTTPBadRequest(
                title='Ressource with the given id not found',
                description=str(e),
            )

    def on_get_collection(self, req, resp):
            resp.status = falcon.HTTP_200
            tasks = []
            tasks_obj = TaskModel.objects
            for obj in tasks_obj:
                tasks.append(obj.to_mongo())

            resp.context.result = tasks

    @spec.validate(
        query=Query, resp=Response(HTTP_200=Resp, HTTP_403=BadLuck)
    )
    def on_post(self, req, resp):
        data = req.context.doc
        title = data['title']
        body = data["body"]

        try:
            task_obj = TaskModel(
                title=title, body=body
            )
            task_obj.save()

            resp.status = falcon.HTTP_201
            resp.context.result = task_obj.to_mongo()

        except Exception as e:
            raise falcon.HTTPBadRequest(
                title='Error occured',
                description=str(e),
            )

    def on_patch(self, req, resp, id):
        data = req.context.doc
        title = data['title']
        body = data["body"]

        try:
            task_obj = TaskModel.objects(id=id)

            task_obj.title=title
            task_obj.body=body
            task_obj.save()

            resp.status = falcon.HTTP_200
            resp.context.result = task_obj.to_mongo()

        except Exception as e:
            raise falcon.HTTPBadRequest(
                title='Ressource with the given id not found',
                description=str(e),
            )

    def on_delete(self, req, resp, id):

        try:
            task_obj = TaskModel.objects(id=id)
            task_obj[0].delete()

            resp.status = falcon.HTTP_200
            resp.context.result = "Ressource deleted succesfully"

        except Exception as e:
            raise falcon.HTTPBadRequest(
                title='Ressource with the given id not found',
                description=str(e),
            )