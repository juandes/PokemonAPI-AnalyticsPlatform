# coding=utf-8

"""
This script modifies the name of some Pokemon's.
For example, some of the them like Deoxys, is named
Deoxys-normal, so I'll change it to Deoxys
"""

import pymongo
from pymongo.collection import ReturnDocument

client = pymongo.MongoClient()
db = client.pokemon
collection = db.pokedex

names_to_change = {
    'Farfetchd': 'Farfetch\'d',
    'Mr-mime': 'Mr. Mime',
    'Ho-oh': 'Ho-Oh',
    'Deoxys-normal': 'Deoxys',
    'Wormadam-plant': 'Wormadam',
    'Mime-jr': 'Mime Jr.',
    'Porygon-z': 'Porygon-Z',
    'Giratina-altered': 'Giratina',
    'Shaymin-land': 'Shaymin',
    'Basculin-red-striped': 'Basculin',
    'Darmanitan-standard': 'Darmanitan',
    'Tornadus-incarnate': 'Tornadus',
    'Thundurus-incarnate': 'Thundurus',
    'Landorus-incarnate': 'Landorus',
    'Keldeo-ordinary': 'Keldeo',
    'Meloetta-aria': 'Meloetta',
    'Flabebe': 'Flabébé',
    'Meowstic-male': 'Meowstic',
    'Pumpkaboo-average': 'Pumpkaboo',
    'Gourgeist-average': 'Gourgeist'
}

for key, value in names_to_change.iteritems():
    result = collection.find_one_and_update({'name': key}, {'$set': {'name': value}},
                                            return_document = ReturnDocument.AFTER)
    if result is None:
        print ('Couldn\'t update {}'.format(key))
    else:
        print ('{} changed to {} \n {}'.format(key, value, result))