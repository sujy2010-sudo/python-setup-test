class Product:

    """
    Product with price validation and computed tax

    Requirements:
    - name property (min 2 characters)
    - price property (must be >= 0)
    - tax_rate property (0.0 to 1.0)
    - price_with_tax (computed property, read-only)
    """
    def __init__(self,name:str,price:float,tax_rate:float =0.10):
        self._name=name
        self._price=price
        self._tax_rate=tax_rate
    
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self,value:str):
        if not value or len(value)< 2: 
            raise ValueError("name must be atleast 2 chars")                  
        self._name=value
    @property

    def price(self)-> float:
        return self._price

    @price.setter

    def price(self,value:float):
        if value <=0:
            raise ValueError("price must be greater than zero")
        self._price=value

    @property

    def tax_rate(self)->float:
        return self._tax_rate

    @tax_rate.setter

    def tax_rate(self,value:float):
        if value <0 or value> 1.0:
            raise ValueError("tax rate must be 0.0 to 1.0")
        self._tax_rate =value
    @property
    def price_with_tax(self)-> float:
        return self.price * (1 + self.tax_rate)

    def __str__(self) -> str:
        return f"{self.name}: ${self.price:.2f} (${self.price_with_tax:.2f} with tax)" 


laptop=Product("macbook",1999.0,0.08)
print(laptop)
print(f"laptop with price({laptop.price:.2f})")
print(f"laptop with price({laptop.price_with_tax:.2f})")

laptop.price=18899.0
try:
    laptop.name
except ValueError as e:
    print(f"error{e}")
    
try:
    laptop.price=-100
except ValueError as e:
    print(f"error{e}")
            
        


    

    
    
