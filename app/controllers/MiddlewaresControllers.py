import json
import falcon
from bson import ObjectId
import datetime

class JSONEncoder(json.JSONEncoder):
    def default(self, o):

        #serializer for ObjectId
        if isinstance(o, ObjectId):
            return str(o)
            
        #serializer for only for datetime object
        if type(o) == datetime.datetime:
            return o.strftime("%Y-%m-%d %H:%M:%S") 
        return json.JSONEncoder.default(self, o)

class RequireJSON:
    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable(
                description='This API only supports responses encoded as JSON.',
                href='http://docs.examples.com/api/json',
            )

        if req.method in ('POST', 'PUT'):
            if 'application/json' not in req.content_type:
                raise falcon.HTTPUnsupportedMediaType(
                    title='This API only supports requests encoded as JSON.',
                    href='http://docs.examples.com/api/json',
                )


class JSONTranslator:

    def process_request(self, req, resp):
        if req.content_length in (None, 0):
            return

        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest(
                title='Empty request body',
                description='A valid JSON document is required.',
            )

        try:
            req.context.doc = json.loads(body.decode('utf-8'))

        except (ValueError, UnicodeDecodeError):
            description = (
                'Could not decode the request body. The '
                'JSON was incorrect or not encoded as '
                'UTF-8.'
            )

            raise falcon.HTTPBadRequest(title='Malformed JSON', description=description)

    def process_response(self, req, resp, resource, req_succeeded):
        if not hasattr(resp.context, 'result'):
            return

        resp.text = json.dumps(resp.context.result, cls=JSONEncoder)