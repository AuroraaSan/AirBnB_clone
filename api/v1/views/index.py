#!/usr/bin/python3
'''api status'''
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

@app_views.route('/status', strict_slashes=False)
def returnstuff():
    '''return stuff'''
    return jsonify(status='OK')

@app_views.route('/stats', strict_slashes=False)
def stuff():
    '''JSON Responses'''
    todos = {
        'states': State,
        'users': User,
        'amenities': Amenity,
        'cities': City,
        'places': Place,
        'reviews': Review
    }
    stats = {}
    for key, model_class in todos.items():
        if not isinstance(model_class, type):
            continue
        stats[key] = storage.count(model_class)
    return jsonify(stats)
