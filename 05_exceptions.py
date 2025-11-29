def divide_numbers(a:float,b:float):
    try:
        result=a/b
        return result
    except ZeroDivisionError:
        print(f"cannot dive {a} by zero")
        return None
    except TypeError as e:
        print(f"error:invalid types{e}")
        return None
    finally:
        print("division attempt completed")
print("basic exceptional handling")
print(divide_numbers(10,2))
print(divide_numbers(10,0))
print(divide_numbers(10,"abc"))

def process_data(data):
    try:
        value=int(data)
        result=100/value
        return result
    except(ValueError,TypeError) as e:
        print(f"input :{e}")
        return None
    except ZeroDivisionError:
        print("cannot divide by zero")
        return None
    
print("multiple exceptions")
process_data("10")
process_data("abc")
process_data("0")


def read_file_safe(filename: str):
    try:
        with open(filename,'r') as file:
            content=file.read()
    except FileNotFoundError:
         print(f"Error:file'{filename} not found")
         return None
    except PermissionError:
        print(f"Error: No permission to read {filename}")   
        return None
    else:
        print(f"successfully read{len(content)} characters")
        return content
    finally:
        print("file operation completed")
    
         
print("\n=== File Reading with else/finally ===")
read_file_safe("nonexistent.txt")

class Employee:
    def __init__(self,name:str,salary:float):
        if not name or len(name)  < 2:
            raise ValueError("name must be more than 1 char")
        if salary < 0:
            raise ValueError("salary cannot be negative")
        if salary < 30000:
            raise ValueError("salary below minimum wage")
        self.name=name
        self.salary=salary
        
    def give_raise(self,amount:float):
        if amount < 0:
            raise ValueError(" amounataa must be > 0")
        self.salary+=amount
        
try:
    emp1=Employee("ALICE",1000)
    print(f"created{emp1.name}")
    emp2=Employee("a",100)
except ValueError as e:
    print(f"validation error{e}")
        
try:
    emp3=Employee("Bob",-100)
except ValueError as e:
    print(f"validation error {e}")      
    
class InsufficientFundsError(Exception):
    def __init__(self,balance:float,amount:float):
        self.balance=balance
        self.amount=amount
        self.message=f"Insufficient funds: Balance ${balance:.2f}, Requested ${amount:.2f}"
        super().__init__(self.message)
class NegativeAmountError(Exception):
    pass
class BankAccount:
    def __init__(self,account_number:str,balance:float=0):
        self.account_number=account_number
        self.balance=balance

    def withdraw(self,amount:float):
        if amount < 0:
            raise NegativeAmountError("Amount cannot be negative")
        if amount >self.balance:
            raise InsufficientFundsError(self.balance,amount)
        self.balance -=amount
        print(f"withdraw amount{amount:,.2f} and balance{self.balance:,.2f}")
    def deposit(self,amount:float):
        if amount < 0:
            raise NegativeAmountError("Amount cannot be negative")
        self.balance+=amount 
        print(f"deposited amount{amount:,.2f} :balance {self.balance:,.2f}")   
account=BankAccount("priya",1000)
try:
    account.withdraw(500)
    account.withdraw(2000)
except InsufficientFundsError as e:
    print(f"error message{e.message}")
    
def process_employee_data(data):
    try:
        employee_id=int(data['id'])
        salary=float(data['salary'])
        return Employee(data['name'],salary)
    except KeyError as e:
        raise ValueError(f"missing required fields{e} ") from e
    except (ValueError,TypeError) as e:
        raise ValueError(f"invalid employee data") from e 
    
    try:
        emp=process_employee_data({"name":"alice"})
    except ValueError as e:
        print(f"error{e}")
        print(f"original cause{e._cause__}")
    def safe_divide(a:float,b:float):
        try:
            if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
                raise TypeError("both arguments will be numbers")
            if b==0:
                raise ZeroDivisionError("cannot divide by zero")
            return a/b
        except(TypeError,ZeroDivisionError) as e:
            print(f"error in division{e}")
            raise
        
        try:
            result=safe_divide(10,0)
        except ZeroDivisionError:
            print("handled at right level")    
                           
        
        
                   
        
                                    