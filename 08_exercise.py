class InvalidAgeError(Exception):
    pass
class InvalidEmailError(Exception):
    pass
class User:
           
    def __init__(self,name:str,age:int,email :str):
        if len(name)< 2:
            raise ValueError("namName must be at least 2 characterse ")
        
        if not(18<=age <=120):
            raise InvalidAgeError("Age must be between 18 and 120 ")
        if "@" not in email or "." not in email:
            raise InvalidEmailError
        self.name=name
        self.age=age
        self.email=email
    def update_age(self,new_age:int):
        if not(18<=new_age <=120):
            raise ValueError("Age must be between 18 and 120")
        self.age=new_age
        
    def update_email(self,new_email):
        if "@" not in new_email or "." not in new_email: 
            raise InvalidAgeError("Age must be between 18 and 120")
        self.new_email=new_email

try:
    user1=User("alice",30,"alice@email.com") 
    print(f"created:{user1.name}")
except (ValueError,InvalidAgeError,InvalidEmailError) as e:
    print(f"error:{e}")
    
try:
    user2=User("A",19,"alice@email.com")    
    print(f"created:{user2.name}")
except (ValueError,InvalidAgeError,InvalidEmailError) as e:
    print(f"error:{e}")  
try:
    user3=User("bob",15,"bob@email.com")   
    print(f"created :{user3.name}")
except (ValueError,InvalidAgeError,InvalidEmailError) as e:
    print(f"error:{e}")

try:
    user4=User("Charlie",30,"invalid-email")
    print(f"created :{user3.name}")
except(ValueError,InvalidAgeError,InvalidEmailError) as e:
     print(f"error:{e}")
     
try:
    user1.update_age(20)
except InvalidAgeError as e:     
    print(f"Error: {e}")
        
          

                 
        