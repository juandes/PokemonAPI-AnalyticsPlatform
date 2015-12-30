import pymongo


def find_pokemon(collection, pokemon):
    return [pokemon for pokemon in
            collection.find({'name': pokemon}, {'name': 1, '_id': 0})]


def find_pokemon_names(collection):
    return collection.find({}, {'name':1, 'national_id': 1,'_id':0}).sort('national_id', pymongo.ASCENDING)

