# This program adds a new array named 'egg_groups' to the
# pokedex collection and removes the old multiple egg group fields.
# The new array has the egg groups to which a Pokemon belongs.

import pymongo
import re

client = pymongo.MongoClient()
db = client.pokemon
collection = db.pokedex

for pokemon in collection.find():
    # List of the egg groups of the current Pokemon
    egg_group_list = []
    for key in pokemon.keys():
        # Check if the key contains 'egg_group' and if the value is 1.
        # If so, the Pokemon belongs to that group
        if 'egg_group' in key and pokemon[key] == 1:
            egg_group_list.append(re.sub('_egg_group', '', key))

    # Remove the previous egg group fields and add the new list
    collection.update_one({'_id': pokemon['_id']},
                          {'$unset': {'ditto_egg_group': '',
                                      'dragon_egg_group': '',
                                      'fairy_egg_group': '',
                                      'flying_egg_group': '',
                                      'field_egg_group': '',
                                      'humanlike_egg_group': '',
                                      'amorphous_egg_group': '',
                                      'mineral_egg_group': '',
                                      'monster_egg_group': '',
                                      'grass_egg_group': '',
                                      'undiscovered_egg_group': '',
                                      'water1_egg_group': '',
                                      'water2_egg_group': '',
                                      'water3_egg_group': ''},
                           '$set': {'egg_groups': egg_group_list}})