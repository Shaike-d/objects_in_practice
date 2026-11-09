class Product:

    def __init__(self,name,price,quantity=0):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        if value < 0:
            raise ValueError("price must be positive")
        else:
            self.__price = value

    @property
    def name(self):
        return self.__name

    
    @property
    def quantity(self):
        return self.quantity
    
    def add_stock(self,amount):
        if amount < 0:
            raise ValueError("amount must be positive")
        else:
            self.__quantity += amount

    def sell(self,amount):
        if amount < 0:
            raise ValueError("amount must be positive")
        if self.__quantity-amount < 0:
            raise ValueError(f"not enough {self.__name}")
        self.__quantity -= amount

    @property
    def total_value(self):
        return self.__price * self.__quantity

    
    def __str__(self):
        return f"{self.__name}: {self.__quantity}*{self.__price} = {self.total_value}"






    

    

    

        




      