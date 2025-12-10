print("\n" + "="*70)
print("PROGRAM 2: USING .get() FOR SAFE ACCESS")
print("="*70)


employee = {
    "name": "Bob Smith",
    "employee_id": 12345,
    "department": "Engineering"
}

salary=employee.get("salary","not specified")
print(f"{salary}")
print(f"{employee['employee_id']}")

bonus=employee.get("bonus",0)
print(f"{bonus}")


# Using .get() with calculations

total_compensation=employee.get("salary",50000) + employee.get("bonus", 4000)
print(f"total_compensation: ${total_compensation:,.2f}")


email=employee.get("email","no email prvoided")
print(f"{email}")

employee_data = {
    "name": "Charlie Davis",
    "id": 5678,
    "active": True
}
#1. Get name (should exist)
print(f"{employee_data['name']}")
#Get salary (doesn't exist, default to 60000)
salary=employee_data.get("salary",60000)
print(f"{salary}")
#Get department (doesn't exist, default to "Unassigned")
department=employee_data.get("department","Unassigned")
#Get years_of_service (doesn't exist, default to 0)
years_of_service=employee_data.get("years_of_service",0)
#Calculate total compensation: salary + (years_of_service * 2000)
total_compensation=employee_data.get("salary",60000)+(employee_data.get("years_of_service",2)*2000)
#total_compensation=employee.get("salary",50000) + employee.get("bonus", 4000)
print(f"{total_compensation}")