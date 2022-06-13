from flask_restful import Resource
from flask import request


class SaveOrUpdate(Resource):
    def post(self):
        customer = request.form
        if validate_customer(customer):
            return "Hello"
        return "Bye"

    def validate_customer(self, customer):
        if customer.last_name == "":
            return False
        return True


class Search(Resource):
    def get(self, search_text):
        if search_text != "":
            return search_text
        return "Bye"


class Customer:
    def __init__(self, customer_form):
        self.id = customer_form['id']
        self.first_name = customer_form['firstName']
        self.last_name = customer_form['lastName']
        self.number = customer_form['pnumber']
