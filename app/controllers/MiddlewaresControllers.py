import json
import falcon
from bson import ObjectId
import datetime

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        print(type(o))
        if isinstance(o, ObjectId):
            return str(o)
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
    # NOTE: Normally you would simply use req.media and resp.media for
    # this particular use case; this example serves only to illustrate
    # what is possible.

    def process_request(self, req, resp):
        # req.stream corresponds to the WSGI wsgi.input environ variable,
        # and allows you to read bytes from the request body.
        #
        # See also: PEP 3333
        if req.content_length in (None, 0):
            # Nothing to do
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
        print(resp.context.result)
        if not hasattr(resp.context, 'result'):
            return

        resp.text = json.dumps(resp.context.result, cls=JSONEncoder)