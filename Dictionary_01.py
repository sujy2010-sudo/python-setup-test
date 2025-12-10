
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s | %(message)s'
)
logger = logging.getLogger(__name__)

print("\n" + "="*70)
print("PROGRAM 1: BASIC DICTIONARY OPERATIONS")
print("="*70)

student = {
    "name": "Alice Johnson",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.8
}
# Access values
print(f"student name:{student['name']}")
print(f"gpa{student['gpa']}")

# Add new key-value pair
student["year"]="senior"
# Update existing value
student["gpa"]=3.9
# Check if key exists
if "email" in student:
     print(f"Email: {student['email']}")
else:
     print("Email not found - adding it...")
     student["email"]  = "alice@university.edu"
     
print(f"\nComplete student info: {student}")        

product={
"name" : "Laptop",
"price" : "999.99",
"brand" : "Dell",
"in_stock" :  True
}

#Print the product name and price
print(f"{product}")    
print(f"product name:{product['name']}")
print(f"product price:{product['price']}")

#Add a "category" key with value "Electronics"
product["category"]="Electronics"
#Update the price to 899.99 (discount!)
product["price"]="899.99"
#Check if "warranty" key exists, if not add it with value "2 years"
if "warranty" in product:
    print(f"warrenty already exists")
else:
    print(f"warrenty not found")
    product["warrenty"]="2 years" 
    
    
print(f"{product}")    