print("\n" + "="*70)
print("PROGRAM 5: DICTIONARIES WITH LISTS (Grouping Pattern)")
print("="*70)

students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "Diana", "grade": "C"},
    {"name": "Eve", "grade": "B"}
]

students_by_grade={}

for student in students:
    grade=student["grade"]
    if grade  not in students_by_grade:
        students_by_grade[grade]=[]
    students_by_grade[grade].append(student['name'])

print("students grouped by grade")

for grade,names in sorted(students_by_grade.items()):
          print(f"grade {grade}:{', '.join(names)}")

# Alternative using .setdefault()
students_by_grade_v2={}
for student in students:
    grade= student["grade"]
    students_by_grade_v2.setdefault(grade,[]).append(student["name"]) 
for grade,names in sorted(students_by_grade_v2.items()):
    #print(f"  Grade {grade}: {names}")    
    print(f"grade {grade}:{', '.join(names)}")    
    
    
employees = [
    {"name": "Alice", "dept": "Engineering", "salary": 75000},
    {"name": "Bob", "dept": "Sales", "salary": 60000},
    {"name": "Charlie", "dept": "Engineering", "salary": 80000},
    {"name": "Diana", "dept": "HR", "salary": 65000},
    {"name": "Eve", "dept": "Sales", "salary": 62000},
    {"name": "Frank", "dept": "Engineering", "salary": 78000}
]

#1. Group employee names by department
employees_by_dept = {}    
for emp in employees:
     dept=emp["dept"]
     employees_by_dept.setdefault(dept,[]).append(emp["name"])
for dept,names in sorted(employees_by_dept.items()):
    print(f"{dept} : {', '.join(names)}( {len(names)} employees)") 
   
    
#3. Find which department has most employees      
max_dept = max(employees_by_dept, key=lambda d: len(employees_by_dept[d]))
print(f"\nDepartment with most employees: {max_dept} ({len(employees_by_dept[max_dept])} employees)")

