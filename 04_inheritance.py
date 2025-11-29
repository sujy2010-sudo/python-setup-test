class Employee:
    company_name="Techcorp"
    
    def __init__(self,name:str,employee_id:int,salary:float):
        self.name=name
        self.employee_id=employee_id
        self.salary=salary
        
    def work(self):
        print(f"{self.name} is working")
        
    def get_details(self)-> str:
        return f"{self.name} (ID:{self.employee_id}- ${self.salary:,.2f})"
    
    def __str__(self)-> str:
        return f"employee{self.name}"
    
class Manager(Employee):
    def __init__(self,name:str,employee_id:int,salary:float,team_size:int):
        super().__init__(name,employee_id,salary)
        self.team_size=team_size
        
    def work(self):
        print(f"{self.name} is managing a team size of {self.team_size}")    
        
    def comduct_meeting(self):
        print(f"{self.name} is conducting a meeting")    
        
    def __str__(self):
       return "manager is {self.name} and team size is {self.team_size}"
   
class Developer(Employee):
    def __init__(self,name: str,employee_id:int,salary:float,programming_language:str):
        super().__init__(name,employee_id,salary) 
        self.programming_language=programming_language
        
        
    def work(self):
        print(f"{self.name}is coding with{self.programming_language}")  
        
    def code_review(self):
        print(f"{self.name} is reviewing code")      
        
    def deubug(self):
        print(f"{self.name} is debugging{self.programming_language}")    
        
    def __str_(self) -> str:
        return f"developer{self.name} ({self.programming_language})"        
    
class Designer(Employee):
    def __init__(self,name:str,employee_id:int,salary:float,designing_tool:str):
        self.designing_tool=designing_tool
        super().__init__(name,employee_id,salary)
        
    def work(self):
        print(f"{self.name} is designing in {self.designing_tool}")
    
    def create_mockup(self):
        print(f"{self.name} is creating UI mockups")
        
    def __str__(self)->str:
        return f"designing {self.name} (tool:{self.designing_tool})"   
    

alice = Manager("Alice", 1001, 95000, team_size=5)
bob=Developer("bob",2,200,programming_language="java") 
charlie=Designer("charlie",3,300,designing_tool="Figma")
employees=[alice,bob,charlie]
print("=== Everyone Working (Polymorphism!) ===")
for emp in employees:      
    emp.work()
print("\n=== Employee Details ===") 

for emp in employees:
    print(emp.get_details())
    
print("\n=== String Representation ===")
for emp in employees:
    print(emp) 
print("\n=== Role-Specific Actions ===")

alice.comduct_meeting()
bob.code_review()
bob.deubug()
charlie.create_mockup()

print("\n=== Type Checking ===")
print(f"is alice an employee? {isinstance(alice,Employee)}") 
print(f"is alice an employee? {isinstance(bob,Employee)}")   
print(f"is alice an employee? {isinstance(charlie,Employee)}")   

class Intern(Developer):
    def __init__(self,name:str,employee_id:int,salary:float,programming_language:str,university:str):
        super().__init__(name,employee_id,salary,programming_language) 
        self.university=university
        self.is_full_=False
    def work(self):
        print(f"{self.name} from {self.university} is learning{self.programming_language}")
        
    def attend_training(self):
        print(f"{self.name} is attending training")
        
david=Intern("David",100,400,"Javascript","MIT")
david.work()
david.attend_training()
david.code_review()
print(isinstance(david,Developer))
print(isinstance(david,Employee))
        
                  


    
    


    
            

 
                    