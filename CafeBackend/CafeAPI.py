import os
import markdown
from flask import Flask
from flask_restful import Resource, Api, abort
from CafeBase import CafeBase
from webargs import fields, validate
from webargs.flaskparser import use_kwargs, parser

base = None

app = Flask(__name__)
api = Api(app)


def get_db():
    global base
    if base is None:
        base = CafeBase()
    return base


@app.route("/cafeapi")
def index():
    with open(os.path.dirname(app.root_path) + '/CafeBackend/README.md') as file:
        content = file.read()
        return markdown.markdown(content)


args_list = {
    'day': fields.Int(
        required=True,
        validate=[validate.Range(min_inclusive=0, max_inclusive=6)]
    ),
}


class Food(Resource):
    @use_kwargs(args_list, location="query")
    def get(self, day):
        return get_db().day_menu(day)


@parser.error_handler
def handle_request_parsing_error(err):
    print(err.messages)
    abort(422, errors=err.messages)


api.add_resource(Food, '/cafeapi/food')

app.run(host='0.0.0.0', port='7777', debug=True)
