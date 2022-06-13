from flask import Flask
from flask_restful import Api
from customer import SaveOrUpdate, Search
from item import ListItems, ListItemTypes, ListAddonItems, ListItemsByType, SaveOrUpdateItem, SaveOrUpdateItemType, SaveOrUpdateAddonItem
from order import ListOrdersByCustomerId,GetOrderById,SaveOrder,CompleteOrder,VoidOrder

app = Flask(__name__)
api = Api(app)

api.add_resource(SaveOrUpdate, '/customer/saveorupdate')
api.add_resource(Search, '/customer/search/<search_text>')

api.add_resource(ListItems, '/item/item/list')
api.add_resource(ListItemTypes, '/item/type/list')
api.add_resource(ListAddonItems, '/item/addonitem/list')
api.add_resource(ListItemsByType, '/item/item/itemtypeid/{item_type_id}/list')
api.add_resource(SaveOrUpdateItem, '/item/item')
api.add_resource(SaveOrUpdateItemType, '/item/type')
api.add_resource(SaveOrUpdateAddonItem, '/item/addonitem')

api.add_resource(SaveOrder, '/order/save')
api.add_resource(CompleteOrder, '/order/complete')
api.add_resource(VoidOrder, '/order/void')
api.add_resource(ListOrdersByCustomerId, '/order//customer/{customer_id}')
api.add_resource(GetOrderById, '/order/{order_id}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
