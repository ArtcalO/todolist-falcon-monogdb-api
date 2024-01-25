import os
import falcon_jsonify
from app.controllers.MiddlewaresControllers import *
dbcfg = {
    'host': 'localhost',
    'port': 27017
}
middleware = [
    RequireJSON(),
    JSONTranslator(),
]