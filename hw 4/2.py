class Product:
    def __init__(self, name, amount, price):
        self.name=name
        self.amount=amount
        self.price=price   
    def get_price(self, m):
        #m=self.amount
        if m<10:
            return self.price
        if m>=10 and m<99:
            return 0.9*self.price
        else:
            return 0.8*self.price
    def make_purchase(self,m):
        return Product.get_price(self,m)
    def totally(self):
        return m*(Product.make_purchase(self,m))
    

name=input("name of product: ")
amount=int(input("amount: "))
price=int(input("price: "))
k=Product(name, amount,price)


print("price will be ", k.make_purchase(amount))
m=int(input("I want ot take "))
print("price will be ", k.make_purchase(m))
print(name, end=" ")
print(m, end=" ")
print(k.totally())