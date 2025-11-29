employee={"name":"Alice Johnson",
          "id":"12345",
          "dept":"engineering",
          "salary":75000,
          "active":True   
          }

print(f"name:{employee['name']}")
print(f"salary ${employee['salary']}")
print(f"Salary: ${employee['salary']:,}")
print(f"email:{employee.get('email','Not provided')}")

if "email" in employee:
    print("email is available")
else:
    print("not available")    
    
employee["email"] ="alice@company.com"    
print(f"email:{employee['email']}")
print(f"email:{employee}")

employee['salary']=40000
print(f"{employee['salary']}")

del employee["active"]
print(f"\n active employees{employee}")

print(employee.keys())
print(employee.values())
print(employee.items())


for key,value in employee.items():
    print(f"{key.capitalize()}:{value}")

employees=[{"name": "Alice","dept":"eng","salary": 7000},
           {"name":"bob","dept":"sales","salary":6000},
           {"name":"charlie","dept":"hr","salary":5000}
   ]    

eng_employees = [emp for emp in employees if emp["dept"]=="eng"]
print(f"\n engineering team: {len(eng_employees)}members")

for emp in eng_employees:
    print(f"- {emp['name']}:${emp['salary']}")
   
total_eng_salary=sum(emp["salary"] for emp in eng_employees)
print(f"\n total eng salary: ${total_eng_salary:,}")    

name_to_salary={emp["name"]:emp["salary"] for emp in employees}
print(f"name to salary{name_to_salary}")

from collections import defaultdict
dept_to_names= defaultdict(list)


from collections import defaultdict
dept_to_names=defaultdict(list)
for emp in employees:
    dept_to_names[emp["dept"]].append(emp["name"])
    
print(f"\n dept to names{dict(dept_to_names)}")    
        
        
company={
     "name":"techcorp",
     "founded":2010,
     "employees":{
         "engineering":50,
         "sales":30,
         "hr":10
         
     },
     "revenue" :10000    
 
 }       
print(f"\company:{company['name']}")
print(f"Engineering employees: {company['employees']['engineering']}")
#print(f"engineering employees{company['name']['engineering']}")
