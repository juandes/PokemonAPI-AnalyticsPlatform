import pymongo

client = pymongo.MongoClient()
db = client.pokemon
collection = db.pokedex


def get_national_pokedex():
    """
	Get the complete national Pokedex (all the Pokemon)
	"""
    for pokemon in collection.find().sort("national_id", pymongo.ASCENDING):
        print pokemon