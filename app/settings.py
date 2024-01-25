import os
import falcon_jsonify
dbcfg = {
    'host': 'localhost',
    'port': 27017
}
middleware = [
    falcon_jsonify.Middleware(help_messages=True),
]