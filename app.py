#!flask/bin/python
from flask import Flask
from flask.ext.restful import Api, Resource, reqparse, fields, marshal


app = Flask(__name__, static_url_path="")
api = Api(app)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

task_fields = {
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
	'id': fields.Integer
    #'uri': fields.Url('task')
}



class NationalPokedexAPI(Resource):
	"""
	GET the complete national Pokedex
	"""
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('title', type=str, required=True,
			help='No', location='json')
		self.reqparse.add_argument('description', type=str, default="",
			location='json')
		super(NationalPokedexAPI, self).__init__()
		
	def get(self):
		return {'tasks': [marshal(task, task_fields) for task in tasks]}
		


#@app.route('/')
#def index():
    #return "Hello, World!"
	
api.add_resource(NationalPokedexAPI, '/MyData/api/v1.0/pokemon/pokedex', endpoint = 'pokedex')

if __name__ == '__main__':
    app.run(debug=True)