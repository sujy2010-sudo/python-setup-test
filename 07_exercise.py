class Vehicle:
    def __init__(self,brand:str,model:str,year:int):
        self.brand=brand
        self.model=model
        self.year=year
        self.mileage=0
        
    def drive(self,miles:float):
        self.mileage+=miles
        print (f"drove {miles} miles.total:{self.mileage}") 
        
    def get_info(self) ->str:
        return f"{self.year}{self.brand}{self.model}"
    
    def __str__(self)->str:
        return f"vechicle{self.get_info()}"
    
class Car(Vehicle):
     
        
    def __init__(self,brand:str,model:str,year:int,num_doors:int,fuel_type:str):
        self.num_doors=num_doors
        self.fuel_type=fuel_type
        super().__init__(brand,model,year)
        
    def drive(self, miles: float):
        print("Driving the car...")
        
    def honk(self):
        print("beep")
        
    def __str__(self)->str:
        return f"Car: {self.get_info()}  Doors: {self.num_doors}  Fuel: {self.fuel_type}"
class Truck(Vehicle):
    def __init__(self,brand: str, model: str, year: int, cargo_capacity: float):
       self.cargo_capacity=cargo_capacity
       super().__init__(brand,model,year) 
    def load_cargo(self, weight: float):
        if weight <= self.cargo_capacity:
            self.current_load = weight
            print(f"Loaded {weight} kg of cargo.")
        else:
            print(f"Cannot load {weight} kg! Max capacity is {self.cargo_capacity} kg.")    
            
    def drive(self, miles: float):
        print(f"Truck driving with {self.current_load} kg cargo...")
        super().drive(miles)
    def __str__(self)->str:
        return f"Truck: {self.get_info()}  Cargo Capacity: {self.cargo_capacity} kg"           
class ElectricCar(Car):
    def __init__(self,brand: str, model: str, year: int, num_doors: int, battery_capacity: float) :
        self.battery_capacity=100
        super().__init__(brand,model,year,num_doors,fuel_type="electric")
        
    def charge(self):
        self.battery_level=100
        print("fully charged")
        
    def __str__(self)->str:
        return f"ElectricCar: {self.get_info()} | Battery: {self.battery_capacity}"
    
car = Car("Toyota", "Camry", 2023, 4, "Gasoline")
print(car)
car.drive(50)
car.honk()

truck = Truck("Ford", "F-150", 2023, 1000)
print(truck)
truck.load_cargo(500)
truck.drive(30)

tesla = ElectricCar("Tesla", "Model 3", 2023, 4, 75)
print(tesla)
tesla.drive(100)
tesla.charge()

vehicles = [car, truck, tesla]
print("\n=== All vehicles driving ===")
for vehicle in vehicles:
    vehicle.drive(10)
            
        
        
        
          
        
    
        
    
    
    
    
              