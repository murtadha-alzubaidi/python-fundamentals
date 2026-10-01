class Product:
    def __init__(self,name,price,quantity):
        self.name= name
        self.price= price
        self.quantity= quantity
    def total_value(self):
        return self.price*self.quantity
    def is_expensive(self):
        return self.price >= 100
products=[Product("laptop",900 , 2),Product("mouse", 25, 10),Product("monitor", 150, 3),]
inventory_total=0
expensive_count=0
for product in products:
    print(product.name, product.total_value())
    inventory_total += product.total_value()
    if product.is_expensive():
     expensive_count +=1
print("Inventory total:", inventory_total)
print("Expensive product:", expensive_count)
