from flask import Blueprint,request,jsonify
from models.inventory import Inventory
from product import Product

bp=Blueprint('products',__name__)

inventory=Inventory()

@bp.route('/produts',method=['GET'])
def get_all_products():
    products=[product._dict_ for product in inventory.product.values()]
    return jsonify(products)

@bp.route('/products',methods=['POST'])
def create_product():
    data=request.get_json()
    product=Product(**data)
    inventory.add_product(product)
    return jsonify(product._dict_),201

@bp.route('/product/<int:product_id>',methods=['GET'])
def get_product(product_id):
    product = inventory.get_product(product_id)
    if product:
        return jsonify(product._dict_)
    else:
        return jsonify({"error":"product not found"}),404

def update_product(product_id):
    data = request.json()
    product = inventory.get_product(product_id)
    if product:
        product.name=data.get('name',product.name)
        product.price=data.get('price',product.price)
        product.category=data.get('category',product.category)
        product.quantity=data.get('quantity',product.quantity)
        return jsonify(product._dict_)
    else:
        return jsonify({"error":"product not found"}),404
    
@bp.route('/product/<int:product_id>',methods=['DELETE'])
def remove_product(product_id):
    inventory.remove_product(product_id)
    return jsonify({"message":"product removed"})