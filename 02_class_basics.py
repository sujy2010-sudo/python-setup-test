class Employee:
    """
    Employee class - direct translation from Java
    This is how a Java developer would first write it
    """

    def __init__(self, name: str, employee_id: int, salary: float, department: str):
        """
        Constructor - equivalent to Java's constructor
        Note: self is like 'this' in Java but MUST be explicit!
        """
        self._name = name              # _ means "private by convention"
        self._employee_id = employee_id
        self._salary = salary
        self._department = department
 
    # Getters (Java-style)
    def get_name(self) -> str:
        """Get employee name"""
        return self._name

    def get_employee_id(self) -> int:
        """Get employee ID"""
        return self._employee_id

    def get_salary(self) -> float:
        """Get employee salary"""
        return self._salary

    def get_department(self) -> str:
        """Get department"""
        return self._department

    # Setters (Java-style)
    def set_name(self, name: str):
        """Set employee name"""
        self._name = name

    def set_salary(self, salary: float):
        """Set salary with validation"""
        if salary > 0:
            self._salary = salary
        else:
            raise ValueError("Salary must be positive")

    def set_department(self, department: str):
        """Set department"""
        self._department = department

    # Business methods
    def give_raise(self, percentage: float):
        """Give a salary raise by percentage"""
        if percentage < 0:
            raise ValueError("Percentage cannot be negative")
        self._salary *= (1 + percentage / 100)
        print(f"{self._name} received a {percentage}% raise!")

    def __str__(self) -> str: #DUNDER methods or magic methods
        """
        String representation - like Java's toString()
        The __str__ method is special in Python
        """
        return (f"Employee(name='{self._name}', id={self._employee_id}, "
                f"salary=${self._salary:,.2f}, dept='{self._department}')")

    def __repr__(self) -> str:
        """
        Official representation - for debugging
        Like toString() but more technical
        """
        return (f"Employee({self._name!r}, {self._employee_id}, "
                f"{self._salary}, {self._department!r})")   
    
emp = Employee("Alice Johnson", 12345, 70000, "Engineering")
    
print(f"Name:{emp.get_name()}")
print(f"salary:{emp.get_salary():,.2f}") 
emp.give_raise(10)
print(f"after 10% raise{emp.get_salary():,.2f}")
print(emp)
print(repr(emp))
    
            
        
        
        
             
         
   
        
    
    
        
        