print("\n" + "="*70)
print("PROGRAM 3: ITERATING THROUGH DICTIONARIES")
print("="*70)
prices = {
    "apple": 0.50,
    "banana": 0.30,
    "orange": 0.75,
    "mango": 1.50
}
for fruit in prices.keys():
    print(f"{fruit}")

for fruit_price in prices.values():
    print(f"{fruit_price:.2f}")  
    
for fruit,price in prices.items():
    print(f"{fruit}:{price}")  
    
grades = {
    "Alice": 95,
    "Bob": 78,
    "Charlie": 88,
    "Diana": 92,
    "Eve": 85
}    
   
#1. Print all student names
for names in grades.keys():
    print(f"{names}")
    
    
#2. Print all grades

for grade_Values in grades.values():
    print(f"{grade_Values}")
    
    
#3. Print name and grade for each student
for name,grade_Values in grades.items():
    print(f"{name}:{grade_Values}")
    
# 4. Calculate the average grade
for grade_Values in grades.values():
    average=sum(grades.values())/len(grades)
print(average)
        
#5. Find students who scored above 85
for name,grade_Values in grades.items():
    #print(f"{name}:{grade_Values}")
    if grade_Values >85:
        print(f"{name}") 
#6. Find the highest grade (use max() on values)
for grade_Values in grades.values():
    highest_grade =max(grades.values())
print(highest_grade)
#7. Find who got the highest grade 
for name,grade_Values in grades.items():
    highest_grade =max(grades.values())
    highest_student=max(grades,key=grades.get)
   
print(highest_grade)  
print(highest_student) 
    