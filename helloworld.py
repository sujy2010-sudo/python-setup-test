name ="alice"
age =28
print (f"name :{name} age {age}")
print (f"name :{name} age {age+1}")

message =f"""
employee profile:
name: {name}
age: {age}
status:active
"""
print(message)
salary=75000.50
print(f"${salary:,.2f}")
bonus_rating=0.15
print(f"{bonus_rating:.1}%") # Output: 15.0%
print(f"{bonus_rating:.1%}") 