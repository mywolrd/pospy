from flask_restful import Resource
from flask import request


class ListItems(Resource):
    def get(self):
        return "items"


class ListItemsByType(Resource):
    def get(self, item_type_id):
        return item_type_id


class ListItemTypes(Resource):
    def get(self):
        return "types"


class ListAddonItems(Resource):
    def get(self):
        return "addonitems"


class SaveOrUpdateItem(Resource):
    def post(self):
        return "list"


class SaveOrUpdateItemType(Resource):
    def post(self):
        return "list"


class SaveOrUpdateAddonItem(Resource):
    def post(self):
        return "list"
