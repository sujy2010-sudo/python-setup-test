# week1_2_refresher_assessment.py
"""
WEEK 1 & 2 REFRESHER ASSESSMENbonusT
Duration: 60 minutes
Topics: Python Basics + OOP

Welcome back! This assessment will help you refresh everything
from Week 1 and Week 2 before we continue.

INSTRUCTIONS:
- Complete as many sections as you can in 60 minutes
- Don't look at notes first - try from memory
- Mark what you struggle with - we'll review together
- Run the code after each section to verify it works

SCORING:
- Section 1 (Week 1 Basics): 40 points
- Section 2 (Week 2 OOP): 40 points
- Section 3 (Integration): 20 points
Total: 100 points

Let's begin! 🚀
"""

import logging
from typing import List, Dict, Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s ",
    handlers=[
        logging.FileHandler("assessment.log"),
        logging.StreamHandler()
    ]
)
logger=logging.getLogger(__name__)
# ============================================================================
# SECTION 1: WEEK 1 PYTHON BASICS REFRESHER (40 points)
# ============================================================================

print("="*70)
print("SECTION 1: PYTHON BASICS (Week 1 Refresher)")
print("="*70)

logger.debug(f"Assessment started")

# -----------------------------------------------------------------------------
# TASK 1.1: Variables, F-Strings, and Formatting (5 points)
# -----------------------------------------------------------------------------
print("\n--- Task 1.1: Variables and F-Strings ---")

# TODO: Create these variables
# - company_name = "TechStartup"
# - employee_count = 1250
# - revenue = 5750000.50
# - founded_year = 2018
# - current_year = 2025
company_name="TechStartup"
employee_count=1250
revenue = 5750000.50
founded_year=2018
current_year = 2025
# Your code here:


# TODO: Print using f-strings with formatting:
# "TechStartup has 1,250 employees and $5,750,000.50 revenue"
# "Founded in 2018, the company has been running for 7 years"

# Your code here:
logger.debug(f"Assessment section 1 completed")



print(f"{company_name} has {employee_count} employees and ${revenue:,.2f} revenue")
print(f"Founded in {founded_year}, the company has been running for {current_year-founded_year} years")
# -----------------------------------------------------------------------------
# TASK 1.2: Lists and List Comprehensions (10 points)
# -----------------------------------------------------------------------------
print("\n--- Task 1.2: Lists and Comprehensions ---")
logger.debug(f"Processing employee data")
# Given data
salaries = [45000, 55000, 65000, 75000, 85000, 95000, 105000]

# TODO 1: Create a list of salaries with 15% raise using list comprehension
#raised_salaries = []  # Your comprehension here
#x+ x*(15/100)

print(f"Original salaries: {salaries}")
raised_salaries = [x+ x*(15/100) for x in salaries]
print(f"After 15% raise: {raised_salaries}")
# TODO 2: Filter salaries above 70000 using list comprehension
#high_salaries = []  # Your comprehension here
high_salaries = [x for x in salaries if x >70000]
print(f"High earners (>70k): {len(high_salaries)} employees")
# TODO 3: Calculate the average salary
average_salary = sum(salaries)/len(salaries) # Your calculation here
print(f"average salary: ${average_salary:,.2f}")
# TODO 4: Print results with formatting
# Expected output:

# "Original salaries: [45,000, 55,000, ...]"
# "After 15% raise: [51,750, 63,250, ...]"
# "High earners (>70k): 4 employees"
# "Average salary: $75,000.00"

# Your print statements here:


# -----------------------------------------------------------------------------
# TASK 1.3: Dictionaries and Loops (10 points)
# -----------------------------------------------------------------------------
print("\n--- Task 1.3: Dictionaries and Loops ---")

# Given employee data
employees = [
    {"name": "Alice", "dept": "Engineering", "salary": 75000, "years": 3},
    {"name": "Bob", "dept": "Sales", "salary": 60000, "years": 2},
    {"name": "Charlie", "dept": "Engineering", "salary": 85000, "years": 5},
    {"name": "Diana", "dept": "HR", "salary": 55000, "years": 4},
    {"name": "Eve", "dept": "Sales", "salary": 65000, "years": 3}
]
# TODO 1: Count employees per department
# Create: {"Engineering": 2, "Sales": 2, "HR": 1}

      
 #TODO 2: Find all employees with 3+ years of experience
   
    
# TODO 3: Calculate total salary by department
dept_salary = {}  # Your code here
for emp in employees:
     dept=emp["dept"]
     dept_salary.setdefault(dept,[]).append(emp["salary"])
for dept,salary in sorted(dept_salary.items()):
    print(f"{dept} : {sum(salary)} ") 
     

# TODO 4: Print results
print("\nDepartment breakdown:")
# Print each department with count and total salary
# Your code here:

dept_count = {}    
for emp in employees:
     dept=emp["dept"]
     dept_count.setdefault(dept,[]).append(emp["name"])
for dept,names in sorted(dept_count.items()):
    print(f"{dept} : {len(names)} ") 
 
print("\nExperienced employees (3+ years):")
# Print names of experienced employees
# Your code here:
experienced = [emp["name"]  for emp in employees if emp["years"] >= 3]
for name in experienced:
    print(name) 
 

# - INFO: "Processing employee data"
# -----------------------------------------------------------------------------
# TASK 1.4: Logging Setup (5 points)
# -----------------------------------------------------------------------------
print("\n--- Task 1.4: Logging Configuration ---")

# TODO: Configure logging with:
# - Level: INFO
# - Format: timestamp | level | message
# - Output to BOTH file (assessment.log) AND console

# Your logging.basicConfig() here:


# TODO: Create a logger
#logger = None  # Your code here

# TODO: Log these messages with appropriate levels:
# - INFO: "Assessment started"
# - INFO: "Processing employee data"
# - WARNING: "Found 2 employees with salary below 60000"
# - INFO: "Assessment section 1 completed"

# Your logging statements here:


# -----------------------------------------------------------------------------
# TASK 1.5: Control Flow and Exception Handling (10 points)
# -----------------------------------------------------------------------------
print("\n--- Task 1.5: Control Flow ---")


# Test your function
test_cases = [
    (70000, 9.5),
    (60000, 8.2),
    (55000, 7.0),
    (50000, 6.5)
]

print("\nBonus calculations:")
def calculate_bonus(salary: float, performance_score: float) -> float:
    """
    Calculate employee bonus based on performance

    Rules:
    - Score >= 9.0: 20% bonus
    - Score >= 8.0: 15% bonus
    - Score >= 7.0: 10% bonus
    - Score < 7.0: 5% bonus
     
    Validation:
    - Salary must be positive
    - Score must be between 0 and 10
    """
    
    if performance_score >=9.0:
        bonus= salary+(salary*20/100)
    elif performance_score>=8.0:
        bonus= salary+(salary*15/100)
    elif performance_score>=7.0:
        bonus= salary+(salary*10/100)
    elif performance_score<7:
        bonus= salary+(salary*5/100)
    elif salary <= 0:
        raise ValueError("salary must be greater than 0")
    
    if score>10:
        raise ValueError("score myst be less than 10")
    
        
                     
    # TODO: Add validation
    # Raise ValueError if salary <= 0
    # Raise ValueError if score < 0 or score > 10

    # Your validation code here:


    # TODO: Implement bonus calculation based on score
    bonus = 0  # Your if/elif/else here


    return bonus

for salary, score in test_cases:
    try:
        bonus = calculate_bonus(salary, score)
        print(f"Salary: ${salary:,}, Score: {score} → Bonus: ${bonus:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")

# Test validation
print("\nTesting validation:")
try:
    calculate_bonus(-1000, 8.0)  # Should fail
except ValueError as e:
    print(f"✓ Caught negative salary: {e}")

try:
    calculate_bonus(70000, 15.0)  # Should fail
except ValueError as e:
    print(f"✓ Caught invalid score: {e}")


# ============================================================================
# SECTION 2: WEEK 2 OOP REFRESHER (40 points)
# ============================================================================

print("\n" + "="*70)
print("SECTION 2: OBJECT-ORIENTED PROGRAMMING (Week 2 Refresher)")
print("="*70)

# -----------------------------------------------------------------------------
# TASK 2.1: Basic Class with @property (10 points)
# -----------------------------------------------------------------------------
print("\n--- Task 2.1: Classes and Properties ---")

class Employee:
    """
    Employee class with proper encapsulation

    TODO: Implement this class with:
    - Private attributes: _name, _salary, _department
    - @property decorators for name, salary, department
    - Validation in setters:
        * name: min 2 characters
        * salary: must be >= 30000
        * department: min 2 characters
    - Method: give_raise(percentage) - increase salary by percentage
    - __str__ method: return "Employee(name, dept, $salary)"
    """

    def __init__(self, name: str, salary: float, department: str):
        # TODO: Use property setters for validation
        self._name=name
        self._salary=salary
        self._department=department

    # TODO: Add @property for name with getter and setter
    @property
    def name(self)->str:
        return self._name
    
    @name.setter
    def name(self,value:str):
        if len(value)<2:
            raise ValueError("name: min 2 characters")
        self._name=value

    # TODO: Add @property for salary with getter and setter
    @property
    def salary(self)->float:
        return self._salary
    
    @salary.setter
    def salary(self,value:float):
        if value < 2000:
            raise ValueError("salary: must be >= 30000")
        self._salary=value
        
            

    # TODO: Add @property for department with getter and setter
    @property
    def department(self)->str:
        return self._department
    
    @department.setter
    def department(self,value:str):
        if len(value) <2:
            raise ValueError("department: min 2 characters")  
        self._department=value

    def give_raise(self, percentage: float):
        """Give salary raise by percentage"""
        # TODO: Validate percentage > 0
        try:
            if percentage <0:
                raise ValueError("percentage cannot be less than 0")
        # TODO: Increase salary
            self._salary=self._salary*(percentage/100)
        # TODO: Log the raise using logger
        except ValueError as e:
            logger.error("percentage cannot be less than 0")
        

    def __str__(self) -> str:
        """String representation"""
        # TODO: Return formatted string
        return f"name: {self.name} (ID: {self.salary}, department: {self.department})"


# Test your Employee class
print("\nTesting Employee class:")
try:
    emp1 = Employee("Alice Johnson", 70000, "Engineering")
  #  print(f"Created: {emp1}")

    emp1.give_raise(10)
    print(f"After raise: {emp1}")

    # Test validation
    emp1.salary = 25000  # Should fail
except ValueError as e:
    print(f"✓ Validation working: {e}")


# -----------------------------------------------------------------------------
# TASK 2.2: Class Methods and Static Methods (10 points)
# -----------------------------------------------------------------------------
print("\n--- Task 2.2: Class and Static Methods ---")

class Product:
    """
    Product class demonstrating @classmethod and @staticmethod

    TODO: Implement:
    - Class variable: tax_rate = 0.10
    - Instance variables: name, price
    - @classmethod from_discounted_price(cls, name, original_price, discount_pct)
    - @staticmethod is_valid_price(price) - returns True if price > 0
    - @property price_with_tax (computed property)
    """

    tax_rate = 0.10  # 10% tax

    def __init__(self, name: str, price: float):
        # TODO: Validate price using static method
        # TODO: Set attributes
        self._name=name
        self._price=price
        pass
    
    @property
    def name(self)->str:
        return self._name
    
    @name.setter
    def name(self,value:str):
        self._name=value
    @property
    def price(self)->float:
        return self._price
    
    @price.setter
    def price(self,value:float):
        self._price=value
           
    # TODO: Add @classmethod from_discounted_price
    # Create product from original price and discount percentage
    # Example: from_discounted_price("Laptop", 1000, 20) → price = 800
    @classmethod
    def from_discounted_price(cls,name:str,price:float,discount:float):
        discounted_price=price-(price*discount)/100
        return cls(name,discounted_price)
        
    # TODO: Add @staticmethod is_valid_price
    # Return True if price > 0
    @staticmethod
    def is_valid_price(price:float)-> bool:
        return 0<=price 
    
   
    @property
    def price_with_tax(self) -> float:
       return self.price * (1 + Product.tax_rate)     
    # TODO: Add @property price_with_tax
    # Return price * (1 + tax_rate)


    def __str__(self) -> str:
        return f"{self.name}: ${self.price:.2f}"


# Test your Product class
print("\nTesting Product class:")
try:
    p1 = Product("MacBook Pro", 1999.99)
    print(f"Created: {p1}")
    print(f"With tax: ${p1.price_with_tax:.2f}")

    p2 = Product.from_discounted_price("iPhone", 999, 15)
    print(f"Discounted product: {p2}")
    print(f"With tax: ${p2.price_with_tax:.2f}")

    # Test validation
    p3 = Product("Invalid", -100)  # Should fail
except ValueError as e:
    print(f"✓ Validation working: {e}")


# -----------------------------------------------------------------------------
# TASK 2.3: Inheritance and Polymorphism (10 points)
# -----------------------------------------------------------------------------
print("\n--- Task 2.3: Inheritance ---")

class Vehicle:
    """Base vehicle class"""

    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        """Start the vehicle"""
        print(f"{self.brand} {self.model} is starting...")

    def get_info(self) -> str:
        """Get vehicle info"""
        return f"{self.year} {self.brand} {self.model}"


# TODO: Create Car class that inherits from Vehicle
class Car(Vehicle):
    """
    Car class - inherits from Vehicle

    TODO: Add:
    
    - Additional attribute: fuel_type
    - Override start() method to print "Car engine starting..."
    - Add method: honk() - print "Beep beep!"
    """
    def __init__(self,brand: str, model: str, year: int,fuel_type:str):
        super().__init__(brand,model,year)
        self._fuel_type=fuel_type
    def start(self):
        print(f"Car engine starting...")    
        
    def honk(self):
        print(f"Beep beep!")      

# TODO: Create ElectricCar that inherits from Car
class ElectricCar(Car):
    """
    Electric car - inherits from Car

    TODO: Add:
    - Additional attribute: battery_capacity
    - Override start() method to print "Electric motor silent start..."
    - Add method: charge() - print "Charging battery..."
    - Override fuel_type in __init__ to always be "Electric"
    """
    def __init__(self,brand: str, model: str, year: int,fuel_type:str,battery_capacity:str):
        super().__init__(brand,model,year,fuel_type="Electric")
        self.battery_capacity=battery_capacity
    def start(self):
        print(f"Electric motor silent start...")    
        
    def charge(self):
        print(f"Charging battery...")     


# Test inheritance
print("\nTesting inheritance:")
vehicles = [
    Car("Toyota", "Camry", 2023, "Gasoline"),
    ElectricCar("Tesla", "Model 3", 2023, "Electric", 75)
]

for vehicle in vehicles:
    print(f"\n{vehicle.get_info()}")
    vehicle.start()
    if isinstance(vehicle, Car):
        vehicle.honk()
    if isinstance(vehicle, ElectricCar):
        vehicle.charge()


# -----------------------------------------------------------------------------
# TASK 2.4: Custom Exceptions (10 points)
# -----------------------------------------------------------------------------
print("\n--- Task 2.4: Custom Exceptions ---")

# TODO: Create custom exception class
class InsufficientBalanceError(Exception):
    """Raised when account balance is insufficient"""

    def __init__(self, balance: float, amount: float):
        # TODO: Store balance and amount
        # TODO: Create message: "Insufficient funds: Balance $X, Requested $Y"
        # TODO: Call super().__init__(self.message)
        self._balance=balance
        self._amount=amount
        self.message=f"Insufficient funds: Balance $X, Requested $Y"
        super().__init__(self.message)


# TODO: Create BankAccount class
class BankAccount:
    """
    Bank account with validation

    TODO: Implement:
    - Private attribute: _balance
    - @property balance (read-only, no setter)
    - deposit(amount) - validate amount > 0
    - withdraw(amount) - validate amount > 0 and amount <= balance
        * Raise InsufficientBalanceError if insufficient funds
    - __str__ method
    """

    def __init__(self, account_number: str, initial_balance: float = 0):
        self.account_number = account_number
        self._balance=initial_balance
        # TODO: Initialize _balance
    @property
    def balance(self):
        return self._balance
    

    # TODO: Add @property balance (read-only)


    def deposit(self, amount: float):
        """Deposit money"""
        if amount <0:
            raise  ValueError("amount less than 0")  
        self._balance +=amount
        logger.debug(f"amount {amount} has been deposited")
        # TODO: Validate amount > 0
        # TODO: Add to balance
        # TODO: Log the deposit
        pass

    def withdraw(self, amount: float):
        """Withdraw money"""
        # TODO: Validate amount > 0
        if amount <0:
            raise  ValueError("amount less than 0") 
        if amount > self._balance:
            raise InsufficientBalanceError("Insufficient funds",amount) 
        self._balance -=amount
        logger.debug(f"amount {amount} has been withdrawn")
        # TODO: Check if sufficient balance (raise InsufficientBalanceError if not)
        # TODO: Deduct from balance
        # TODO: Log the withdrawal
        

    def __str__(self) -> str:
        return f"Account {self.account_number}: ${self.balance:,.2f}"


# Test BankAccount
print("\nTesting BankAccount:")
account = BankAccount("ACC001", 1000)
print(account)

try:
    account.deposit(500)
    print(account)

    account.withdraw(300)
    print(account)

    account.withdraw(2000)  # Should fail
except InsufficientBalanceError as e:
    print(f"✓ Caught insufficient funds: {e}")
except ValueError as e:
    print(f"✓ Validation working: {e}")


# ============================================================================
# SECTION 3: INTEGRATION - REAL-WORLD SCENARIO (20 points)
# ============================================================================

print("\n" + "="*70)
print("SECTION 3: INTEGRATION - Employee Management System")
print("="*70)

"""
SCENARIO:
Build a mini employee management system that combines everything:
- Week 1: Lists, dicts, comprehensions, logging
- Week 2: Classes, properties, inheritance, exceptions

REQUIREMENTS:
1. Manager class (inherits from Employee)
   - Additional attribute: team_size
   - Override give_raise to give 1.5x the percentage to managers
   - Add method: add_team_member() - increase team_size

2. Department class
   - Manages list of employees
   - Methods: add_employee, remove_employee, get_total_salary
   - Method: get_top_performers(min_score) - return employees with score >= min_score

3. Use proper logging throughout
4. Handle exceptions appropriately
"""

# TODO: Implement Manager class
class Manager(Employee):
    """Manager - inherits from Employee"""
    def __init__(self,name:str,department:str,salary:float,team_size:int):
        super().__init__(name,department,salary)
        if team_size < 0:
            raise ValueError("team_size cannot be negative")
        self.team_size=team_size
        
    def add_team_member(self,):
        self.team_size+=1
        print(f"added team member {self.name} .Team size is {self.team_size}")    
        
    def __str__(self):
       return "manager is {self.name} and team size is {self.team_size}"
   
    def give_raise(self, percentage: int):
        """Give salary raise by percentage"""
        effective_pct = percentage * 1.5
        # TODO: Increase salary
        new_salary=self._salary*(1+effective_pct/100)
        self.salary = new_salary
        logger.info(f"Manager {self.name} given {effective_pct:.2f}% raise -> ${self.salary:,.2f}")



# TODO: Implement Department class
class Department:
    """
    Department managing multiple employees

    Attributes:
    - name: Department name
    - employees: List of Employee objects

    Methods:
    - add_employee(employee) - add to list
    - remove_employee(name) - remove by name
    - get_total_salary() - sum all employee salaries
    - get_average_salary() - calculate average
    - list_employees() - print all employees
    """

    def __init__(self, name: str):
        self.name = name
        self.employees: List[Employee] = []

    # TODO: Implement all methods
    def add_employee(self,employee:Employee):
        if not isinstance(employee, Employee):
            raise ValueError("Only Employee (or subclasses) can be added")
        self.employees.append(employee)
        logger.info(f"Added {employee.name} to {self.name}")
    def remove_employee(self, name: str) -> bool:
        """Remove employee by name. Returns True if removed, False if not found."""
        for i, emp in enumerate(self.employees):
            if emp.name == name:
                removed = self.employees.pop(i)
                logger.info(f"Removed {removed.name} from {self.name}")
                return True
        logger.warning(f"Employee {name} not found in {self.name}")
        return False

    def get_total_salary(self) -> float:
        total = sum(emp.salary for emp in self.employees)
        logger.debug(f"Total salary for {self.name}: {total}")
        return total

    def get_average_salary(self) -> float:
        if not self.employees:
            return 0.0
        avg = self.get_total_salary() / len(self.employees)
        logger.debug(f"Average salary for {self.name}: {avg}")
        return avg

    def list_employees(self):
        if not self.employees:
            print(f"No employees in {self.name}")
            return
        print(f"Employees in {self.name}:")
        for emp in self.employees:
            if isinstance(emp, Manager):
                print(f" - {emp.name} (Manager) | ${emp.salary:,.2f} | team_size={emp.team_size}")
            else:
                print(f" - {emp.name} | ${emp.salary:,.2f} | dept={emp.department}")

    def get_top_performers(self, min_score: float):
        """
        Return list of employees with attribute `score` >= min_score.
        If an Employee has no `score` attribute it will be ignored.
        """
        top = [emp for emp in self.employees if hasattr(emp, "score") and getattr(emp, "score") >= min_score]
        logger.info(f"Found {len(top)} top performers (score >= {min_score}) in {self.name}")
        return top

    def __str__(self) -> str:
        return f"Department: {self.name} ({len(self.employees)} employees)"

# Test Integration
print("\nTesting Employee Management System:")

# Create department
eng_dept = Department("Engineering")

# Add employees
try:
    emp1 = Employee("Alice", 75000, "Engineering")
    emp2 = Employee("Bob", 70000, "Engineering")
    mgr1 = Manager("Charlie", 95000, "Engineering", team_size=5)

    eng_dept.add_employee(emp1)
    eng_dept.add_employee(emp2)
    eng_dept.add_employee(mgr1)

    print(f"\n{eng_dept}")
    eng_dept.list_employees()

    print(f"\nTotal salary: ${eng_dept.get_total_salary():,.2f}")
    print(f"Average salary: ${eng_dept.get_average_salary():,.2f}")

    # Give raises
    print("\nGiving 10% raises...")
    for emp in eng_dept.employees:
        emp.give_raise(10)

    print(f"\nAfter raises:")
    eng_dept.list_employees()
    print(f"New total: ${eng_dept.get_total_salary():,.2f}")

except ValueError as e:
    print(f"Error: {e}")


# ============================================================================
# ASSESSMENT COMPLETE
# ============================================================================

print("\n" + "="*70)
print("ASSESSMENT COMPLETE!")
print("="*70)

print("""
📊 SCORING GUIDE:
   Section 1 (Python Basics): ___/40 points
   Section 2 (OOP): ___/40 points
   Section 3 (Integration): ___/20 points
   TOTAL: ___/100 points

📝 SELF-ASSESSMENT:
   Mark which topics you struggled with:
   [ ] Variables and F-strings
   [ ] List comprehensions
   [ ] Dictionaries and loops
   [ ] Logging configuration
   [ ] Control flow and validation
   [ ] Classes and @property
   [ ] @classmethod and @staticmethod
   [ ] Inheritance and polymorphism
   [ ] Custom exceptions
   [ ] Integration of concepts

🎯 NEXT STEPS:
   1. Review this file with your mentor
   2. Discuss areas where you struggled
   3. Do quick refresher on weak topics
   4. Ready to continue with new material!

Great job attempting this assessment!
""")