import pymongo


def find_pokemon(collection, pokemon):
    return [pokemon for pokemon in
            collection.find({'name': pokemon}, {'name': 1, '_id': 0})]


def find_pokemon_names(collection):
    return collection.find({}, {'name':1, 'national_id': 1,'_id':0}).sort('national_id', pymongo.ASCENDING)


def find_pokemon(name, collection):
    return collection.find_one({'name': name})
    
    
def find_pokemon_by_type(type, collection):
    return collection.find({'primary_type': type})
    
def get_all_types(collection):
    return collection.find({}, {'type':1, '_id':0}).sort('type', pymongo.ASCENDING)

