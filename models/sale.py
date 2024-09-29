# from filename import class 
from models.transaction import Transaction
from datetime import datetime

class Sale(Transaction):
    sales = []

    def __init__(self,id,product_id,quantity,price):
        super().__init__(id,product_id,quantity,price)
        self.date = datetime.now()
        # classname.emptyList.append
        Sale.sales.append(self)
    
    @staticmethod
    def get_all_sales():
        return Sale.sales
    
    def to_dict(self):
        return{
            "id" : self.id,
            "product_id" : self.product_id,
            "quantity" : self.quantity,
            "price" : self.price,
            "date":self.date
        }
    
sale1 = Sale("1","101","12","10.00")
# sale2 = Sale("1","101","12","10.00")
print(sale1.to_dict())
