print("\n" + "="*70)
print("PROGRAM 10: PERFORMANCE OPTIMIZATION WITH DICTIONARIES")
print("="*70)

employees_list = [
    {"id": 1, "name": "Alice", "dept": "Eng"},
    {"id": 2, "name": "Bob", "dept": "Sales"},
    {"id": 3, "name": "Charlie", "dept": "Eng"},
    {"id": 4, "name": "Diana", "dept": "HR"},
    {"id": 5, "name": "Eve", "dept": "Sales"}
    # ... imagine 10,000 more employees
]
def find_by_dept_slow(dept):
    return [emp for emp in employees_list if emp["dept"] == dept]
def build_dept_index(employees):
    index={}
    for emp in employees:
        dept=emp["dept"]
        if dept not in index:
            index[dept]=[]
        index[dept].append(emp)
    return index
dept_index= build_dept_index(employees_list)    
slow_result=find_by_dept_slow("Eng")
def find_by_dept_fast(dept):
    """O(1) - instant lookup"""
    return dept_index.get(dept, [])
fast_result=find_by_dept_fast("Eng") 
print(f"Slow result: {len(slow_result)} employees")
print(f"fast result: {len(fast_result)} employees")  
students = [
    {"id": 101, "name": "Alice", "gpa": 3.8},
    {"id": 102, "name": "Bob", "gpa": 3.5},
    {"id": 103, "name": "Charlie", "gpa": 3.9},
]
def find_by_id_slow(student_id):
    return [student for student in students if student_id["student_id"]]
students_by_id = {student["id"]: student for student in students}
def find_by_id_fast(student_id):
    return students_by_id.get(student_id)

products = [
    {"id": "P001", "name": "Laptop", "category": "Electronics", "price": 999},
    {"id": "P002", "name": "Mouse", "category": "Electronics", "price": 25},
    {"id": "P003", "name": "Desk", "category": "Furniture", "price": 299},
    {"id": "P004", "name": "Chair", "category": "Furniture", "price": 199},
    {"id": "P005", "name": "Monitor", "category": "Electronics", "price": 399},
]
by_id = {}
product_by_id = {prod["id"]: prod for prod in products}
def find_product(product_id):
    return product_by_id.get(product_id)

def build_category_index(products_list):
    index={}
    for prod in products_list:
        category=prod["category"]
        if category not in index:
            index[category]=[]
        index[category].append(prod)
    return index
category_index= build_category_index(products)    
def find_by_category_fast(category):
   
    return category_index.get(category, [])
"""
def build_price_index(products_list):
    index={}
    for prod in products_list:
        price=prod["price"]
        if price not in index:
            index[price]=[]
        index[price].append(prod)
    return index
dept_index= build_price_index(employees_list)    
def find_by_dept_fast(price):
  
    return dept_index.get(price, [])
"""
print(find_product("P001"))
print(find_by_dept_fast("Electronics"))
# Simplified example (imagine 1000 products)
products = [
    {"id": "P001", "name": "Laptop", "category": "Electronics", "price": 999},
    {"id": "P002", "name": "Mouse", "category": "Electronics", "price": 25},
    {"id": "P003", "name": "Desk", "category": "Furniture", "price": 299},
    {"id": "P004", "name": "Chair", "category": "Furniture", "price": 199},
    {"id": "P005", "name": "Monitor", "category": "Electronics", "price": 399},
]



by_price_range = {"0-100": [], "100-500": [], "500+": []}

# Then write these functions:


def find_by_price_range(min_price, max_price):
    return [
        prod
        for prod in products
        if min_price <= prod["price"] <= max_price
    ]


print(find_by_price_range(0, 100))





