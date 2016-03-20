import pymongo
from bson import json_util
import json
from engine import *
from flask import Flask, jsonify, make_response, render_template
from flask.ext.restful import Api, Resource, reqparse
from bson.json_util import dumps

app = Flask(__name__)

client = pymongo.MongoClient()
db = client.pokemon
collection = db.pokedex
types_collection = db.types


def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp


DEFAULT_REPRESENTATIONS = {'application/json': output_json}
api = Api(app)
api.representations = DEFAULT_REPRESENTATIONS


# Web Service

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
                collection.find({'region': region.capitalize()})
                    .sort('national_id', pymongo.ASCENDING)]


class PokemonByNumber(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, location='json')
        super(PokemonByNumber, self).__init__()


    def get(self, id):
        """
        GET a regional Pokedex
        :param region: Pokemon region
        :return: Pokedex for region
        """
        pokemon = collection.find_one({'national_id': id})
        if pokemon:
            return {'status':'ok', 'data':pokemon}
        else:
            return {'status':'error'}


class PokemonByName(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, location='json')
        super(PokemonByName, self).__init__()

    def get(self, name):
        pokemon = collection.find_one({'name' : name.capitalize()})
        if pokemon:
            return {'status': 'ok', 'data': pokemon}
        else:
            return {'status': 'error'}


api.add_resource(NationalPokedexAPI,
                 '/pokemon/api/v1.0/pokedex', endpoint='pokedex')
api.add_resource(RegionalPokedexAPI,
                 '/pokemon/api/v1.0/pokedex/<string:region>', endpoint='region')
api.add_resource(PokemonByNumber,
                 '/pokemon/api/v1.0/pokemon/by-id/<int:id>', endpoint='id')
api.add_resource(PokemonByName,
                 '/pokemon/api/v1.0/pokemon/<string:name>', endpoint='name')


@app.route('/')
def index():
    return render_template('template.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/endpoints')
def endpoints_page():
    return render_template('endpoints.html')

@app.route('/pokedex')
def all_pokemon_page():
    return render_template('pokedex.html', pokemon_dump = [pokemon for pokemon in find_pokemon_names(collection)])
    
@app.route('/types')
def types_page():
    return render_template('types.html', types = [type for type in get_all_types(types_collection)])
    
@app.route('/type/<string:type>/')
def type_page(type):
    return render_template('type.html', type = type, pokemons_by_type = [pokemon for pokemon in find_pokemon_by_type(type, collection)])

@app.route('/pokemon/<string:pokemon_name>/')
def pokemon_page(pokemon_name):
    return render_template('pokemon.html', pokemon_data = find_pokemon(pokemon_name, collection))

if __name__ == '__main__':
    app.run(debug=True)
