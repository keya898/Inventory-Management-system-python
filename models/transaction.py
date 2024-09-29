from datetime import datetime 
# class for transaction

class Transaction:
    transactions = []

    def __init__(self,id,product_id,quantity,price):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.date = datetime.now()
        Transaction.transactions.append(self)
    
    @staticmethod
    def get_all_transactions():
        return Transaction.transactions
    
    def to_dict(self):
        return {
            "id" : self.id,
            "product_id" : self.product_id,
            "quantity" : self.quantity,
            "price" : self.price,
            "date":self.date.strftime('%Y-%m-%d %H:%M:%S')
        }
    
# tr1 = Transaction("1","101","12","10.00")
# print(tr1.to_dict())