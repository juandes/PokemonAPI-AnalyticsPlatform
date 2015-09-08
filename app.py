from flask.ext.restful import Api
from flask import Flask, make_response
from flask.ext.restful import Resource, reqparse, fields
from bson.json_util import dumps
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient()
db = client.pokemon
collection = db.pokedex


def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp


DEFAULT_REPRESENTATIONS = {'application/json': output_json}
api = Api(app)
api.representations = DEFAULT_REPRESENTATIONS

# Service

class NationalPokedexAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        #self.reqparse.add_argument('title', type=str, required=True, help='No',
         #                          location='json')
        #self.reqparse.add_argument('description', type=str, default="",
         #                          location='json')
        super(NationalPokedexAPI, self).__init__()

    def get(self):
        """
        GET the complete national Pokedex
        :return: Complete national Pokedex
        """
        return [pokemon for pokemon in
                collection.find().sort("national_id", pymongo.ASCENDING)]


api.add_resource(NationalPokedexAPI,
                 '/Pokemon/api/v1.0/pokemon/pokedex', endpoint='pokedex')


@app.route('/')
def index():
    return "Hi"


if __name__ == '__main__':
    app.run(debug=True)
