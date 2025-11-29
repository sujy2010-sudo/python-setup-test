class EmployeePythonic:
    def __init__(self,name:str,salary:float):
        self._name=name
        self._salary=salary
        
    @property
    def name(self) -> str:
         return self._name
     
    @name.setter
    def name(self,value: str) :
        if not value  or len(value) < 2:
            raise ValueError("name cannot be 1 char")
        self._name =value
        
    @property
    def salary(self) -> float:
        return self._salary
        
    @salary.setter
    def salary(self,value : float):
        if value < 0:
            raise ValueError("value cannot be < 0")
        self._salary=value
        
    @property
    def annual_bonus(self) -> float:
        return self._salary*0.10   
    
print("\n python syle")
emp_py =EmployeePythonic("alice",1000)   
print(f"name '{emp_py.name}' : salary {emp_py.salary:,.2f}") 
emp_py.salary=2000
print(f"name '{emp_py.name}' : salary {emp_py.salary:,.2f}") 
print(f"name '{emp_py.name}' : salary {emp_py.annual_bonus:,.2f}")  
    
try:
    emp_py.name="A"
except ValueError as e:
    print(f"value error{e}")

try:
    emp_py.salary=-1
except ValueError as e:
    print(f"value error salary{e}")    
        
class Rectangle:
    def __init__(self,width: float,height:float):
        self._width=width
        self._height=height
    
    @property
    
    def width(self) -> float:
        return self._width
    
    @width.setter
    
    def width(self,value:float):
        if value <=0:
            ValueError("error")
        self._width=value
    
    @property
    def height(self)-> float:
        return self._height
    
    @height.setter
    def height(self,value:float):
        if value<=0:
            ValueError("error")
        self._height=value
    @property       
    def area(self) ->float:
        return self._height*self._width
    
    @property
    def perimeter(self) -> float:
        return 2 *(self._width+self._height)
    
rect =Rectangle(10,20)
print("{rect._height} x {rect._width}")
print(rect.area)
rect._height=20
print(rect.perimeter)

try:
    rect.area=10
except AttributeError as e:
    print(f"area is read only")
    
    
    
                
        
        
     
     
     
 
    
    
  
        
    