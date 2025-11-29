class Temperature:
    conversions_count = 0
    
    def __init__(self,celsius:float):
        self.celsius=celsius
        Temperature.conversions_count +=1
        
    @classmethod
    def from_farenheit(cls,farenheit:float):
        celcius=(farenheit - 32) * 5/9  
        return cls(celcius)
    
    @classmethod
    def from_kelvin(cls,kelvin:float):
        celsius = kelvin - 273.15
        return cls(celsius)
    
    @staticmethod
    def is_valid_celcius(celcius:float) -> bool:
        return celcius >=-273.15
    @property
    def fahrenheit(self)->float:
        return  (self.celsius * 9/5) + 32
    
    @property
    def kelvin(self)-> float:
        return self.celsius + 273.15
    
    def __str__(self)-> str:
         return f"{self.celsius}°C = {self.fahrenheit}°F = {self.kelvin}K"
     
temp1=Temperature(25)
print(temp1)
temp2=Temperature.from_farenheit(100)
print(temp2)
temp3=Temperature.from_kelvin(300)
print(temp3)
print(f"\nIs -300°C valid? {Temperature.is_valid_celcius(-300)}")
print(f"Is 25°C valid? {Temperature.is_valid_celcius(25)}")

print(f"\nTotal conversions: {Temperature.conversions_count}")
   
    
    
            