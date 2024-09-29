# class for product

class Product:
    def __init__(self,id,name,price,category,quantity):
        self.id=id
        self.name=name
        self.price=price
        self.category=category
        self.quantity=quantity

    def __str__(self):
        return f'product {self.id}: {self.name},Price: {self.price},Quantity: {self.quantity}'

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "price":self.price,
            "category":self.category,
            "quantity":self.quantity
        }
# product1 = Product("101","Lays","10.00","Food","12")
# print(product1.to_dict())