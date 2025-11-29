class Employee:
    company_name ="TechCorp"
    employee_count=0
    
    def __init__(self, name: str, salary: float):
        self.name=name
        self.salary=salary
        Employee.employee_count +=1
        
    def give_raise(self,percentage:float):
        self.salary *=(1+percentage/100)
        print(f"{self.name}salary:${self.salary:,.2f}")    
        
        
    @classmethod
    def from_monthly_salary(cls,name:str,monthly_salary:float):
        annual_salary=monthly_salary * 12
        return cls(name,annual_salary)
    
    @classmethod
    def get_employee_count(cls):
        return cls.employee_count
    
    @classmethod
    
    def set_company_name(cls,name:str):
        cls.company_name=name
        
        
    @staticmethod
    def is_valid_salary(salary:float)-> bool:
        return salary >=30000 and salary <=100000  
    @staticmethod 
    def calculate_tax(salary:float,tax_rate:float=0.30) -> float:
        return salary * tax_rate
    
    def __str__(self) -> str:
        return(f"{self.name} at{self.company_name}:${self.salary:,.2f}")
        
emp1=Employee("Alice",1000)
#emp1.give_raise(10)
emp2=Employee.from_monthly_salary("bob",5000)
#print(emp2)
#print(f"total employees{Employee.get_employee_count()}")
Employee.set_company_name("megacorp")
#print(emp1)
#print(emp2)
#print(f"{Employee.is_valid_salary(5000)}")     
#print(f"{Employee.is_valid_salary(25000)}")           

salary=8000
tax=Employee.calculate_tax(salary)
#print(f"tx on salary{salary} is {tax}")

from datetime import datetime

class MeetingScheduler:
    """Demonstrates factory methods"""

    def __init__(self, meeting_time: datetime, duration_minutes: int):
        self.meeting_time = meeting_time
        self.duration_minutes = duration_minutes

    @classmethod
    def from_string(cls, time_string: str, duration_minutes: int):
        """Create meeting from string: '2025-01-15 14:30'"""
        meeting_time = datetime.strptime(time_string, "%Y-%m-%d %H:%M")
        return cls(meeting_time, duration_minutes)
    
    @classmethod
    def quick_meeting(cls,time_string:str):
        return cls.from_string(time_string,30)
    @staticmethod
    def is_business_hour(hour:int)-> bool:
        return 9<=hour <17
    
    def __str__(self) ->str:
        return f"meeting at {self.meeting_time} for {self.duration_minutes}mins"
    
meeting1 = MeetingScheduler.from_string("2025-01-15 14:30", 60)
print(f"\n{meeting1}")    
meeting2 = MeetingScheduler.quick_meeting("2025-01-15 10:00")
print(meeting2)

print(f"is  14:00 business hours? {MeetingScheduler.is_business_hour(14)}")
print(f"is  20:00 business hours? {MeetingScheduler.is_business_hour(20)}")