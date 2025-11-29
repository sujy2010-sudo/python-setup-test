class BankAccount:
    
    
    def __init__(self,account_number:int,account_holder :str,initial_balance:float):
        pass
    
    def deposit(self,amount:float): 
        pass
    def withdraw(self,amount:float) -> bool:
        pass
    def getBalance(self) -> float:
        pass
    def get_account_number(self) -> str:
        pass
    def __str__(self) -> str:
        pass
    
account=BankAccount("acc01","riya",100)
print(account)
account.deposit(500)
print(f"{account.getBalance}:,.2f")
account.withdraw(500)
print(f"{account.getBalance}:,.2f")
    
    