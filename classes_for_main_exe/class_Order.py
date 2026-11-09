import classes_for_main_exe.class_Customer as c
class Order:

    def __init__(self,customer,price):
        self.customer = customer
        self.price = price

def answer_2():
    order_1 = Order(c.dana,100)
    order_2 = Order(c.dana,120)
    print(order_1.customer.city,order_2.customer.city)
    dana = c.Customer("dana","Tel-aviv")
    print(dana.city,dana.city)
    
