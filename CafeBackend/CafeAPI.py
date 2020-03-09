import os
import markdown
import shelve
from flask import Flask, g
from flask_restful import Resource, Api
from flask import request

app = Flask(__name__)
api = Api(app)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("users")
    return db


@app.route("/cafeapp")
def index():
    with open(os.path.dirname(app.root_path) + '/CafeAPI/README.md') as file:
        content = file.read()
        return markdown.markdown(content)


class Food(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())
