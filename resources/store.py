from flask_restful import Resource
from models.store import StoreModel

class Store(Resource): # note that it extends (inherits) the resource class
    def get (self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return{'message': 'Store not found'}, 404 # returns a tuple first in the body the secone in the status code.

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'message':f'{name} store already exists'}, 400
        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {'message': 'An error occured while creating the store.'}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': f'Store {name} was deleted'}

class StoreList(Resource):
    def get(self):
        return {'stores':[store.json() for store in StoreModel.query.all()]}
