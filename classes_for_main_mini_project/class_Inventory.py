class Inventory:
   

    def __init__(self):
        self.__products = []
        
    
    
    

    def add(self,product):
        if self.find(product.name) != None:
            raise ValueError(f"{product.name} already exists")
        else:
            self.__products.append(product)

    def find(self,name):
        for product in self.__products:
            if product.name == name:
                return product
            
    def by_value(self):
          sorted_by_val = sorted(self.__products,key=lambda p:p.total_value,reverse=True)
          return sorted_by_val

    @property
    def total_value(self):
        values = []
        for product in self.__products:
            values.append(product.total_value)
        return sum(values)
