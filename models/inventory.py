from models.product import Product
from models.sale import Sale
from models._return import Return

class Inventory:
    def __init__(self):
        self.product = {} #initialise product as empty dict to store product using id as their key and product obj as obj as their value
        self.sales = [] #Initialise as a empty list to store all recorded transactions
        self.returns = [] #Initialise returns as a empty list to store all recorded product returns

    def add_product(self,product):
        self.product[product.id] = product

    def update_product(self,product_id,quantity):
        if product_id in self.product:
            self.product[product_id].quantity = quantity
        else:
            print("Product not found")
        
    def delete_product(self,product_id):
        if product_id in self.product:
            del self.product[product_id]
        else:
            print("Product not found")

    def view_product(self):
        for product in self.product.values():
            print(product)

    def get_product(self,product_id):
        return self.product.get(product_id)
    
    def record_sale(self,product_id,quantity,price):
        product = self.get_product(product_id)
        if product :
            if product.quantity >= quantity : #check if there is enough stock in inventry to fulfill the sale. It compares the current quantity of product with requested quantity
                sale = Sale(len(self.sales)+1,product_id,quantity,price)
                product.quantity -= quantity
                self.sales.append(sale)
                return sale
            else:
                print("Not enough quantity in stock")
        else:
            print("product not found")

    def record_return(self,product_id,quantity,reason): # product_id to identify the product quantity the number of units returneds reason the return for reason
        product = self.get_product(product_id)
        if product :
            return_obj = Return(len(self.returns)+1,product_id,quantity,reason)
            product.quantity += quantity
            self.returns.append(return_obj)
        else:
            print("Product not found")

    def view_sales(self):
        for sale in self.sales:
            print(sale)

    def view_returns(self):
        for return_obj in self.returns:
            print(return_obj)