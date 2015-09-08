import pymongo
from flask import Flask, make_response
from flask.ext.restful import Api, Resource, reqparse
from bson.json_util import dumps

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


class NationalPokedexAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(NationalPokedexAPI, self).__init__()

    def get(self):
        """
        GET the complete national Pokedex
        :return: Complete national Pokedex
        """
        return [pokemon for pokemon in
                collection.find().sort('national_id', pymongo.ASCENDING)]


class RegionalPokedexAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('region', type=str, location='json')
        super(RegionalPokedexAPI, self).__init__()

    def get(self, region):
        """
        GET a regional Pokedex
        :param region: Pokemon region
        :return: Pokedex for region
        """
        return [pokemon for pokemon in
                collection.find({'region': region})
                    .sort('national_id', pymongo.ASCENDING)]


api.add_resource(NationalPokedexAPI,
                 '/pokemon/api/v1.0/pokedex', endpoint='pokedex')
api.add_resource(RegionalPokedexAPI,
                 '/pokemon/api/v1.0/pokedex/<string:region>',
                 endpoint='region')


@app.route('/')
def index():
    return "Hi"


if __name__ == '__main__':
    app.run(debug=True)