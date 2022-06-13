from flask_restful import Resource
from flask import request


class ListOrdersByCustomerId(Resource):
    def get(self, customer_id):
        return customer_id


class GetOrderById(Resource):
    def get(self, order_id):
        return order_id


class SaveOrder(Resource):
    def post(self):
        return "save"


class CompleteOrder(Resource):
    def post(self):
        return "complete"


class VoidOrder(Resource):
    def post(self):
        return "void"
