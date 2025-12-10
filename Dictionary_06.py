print("\n" + "="*70)
print("PROGRAM 6: NESTED DICTIONARIES (Dictionaries within Dictionaries)")
print("="*70)

company = {
    "Engineering": {
        "employees": 15,
        "budget": 500000,
        "manager": "Alice Johnson"
    },
    "Sales": {
        "employees": 10,
        "budget": 300000,
        "manager": "Bob Smith"
    },
    "HR": {
        "employees": 3,
        "budget": 150000,
        "manager": "Charlie Davis"
    }
}
# Access nested values
print(f"Engineering manager: {company['Engineering']['manager']}")
print(f"Sales budget: ${company['Sales']['budget']:,}")

# Iterate through nested dictionary

for dept_name,dept_info in company.items():
    print(f"\n dept_name: {dept_name}")
    print(f"\n manager: {dept_info['manager']}")
    print(f"\n employees: {dept_info['employees']}")
    print(f"\n budget: {dept_info['budget']}")
    
total_employees=sum(dept['employees'] for dept in company.values())    
total_budget=sum(dept['budget'] for dept in company.values())

print(f"  Total employees: {total_employees}")
print(f"  Total budget: ${total_budget:,}")

products = {
    "P001": {
        "name": "Laptop",
        "price": 999.99,
        "stock": 5,
        "category": "Electronics"
    },
    "P002": {
        "name": "mobile",
        "price": 1000,
        "stock": 2,
        "category": "Electronics1"
    },
    "P003": {
        "name": "tv",
        "price": 2000,
        "stock":15,
        "category": "Electronics"
    },
}
    
#Print each product with all details
  
for product_name,product_info in products.items():
    print(f"\n product: {product_name}")
    print(f"\n name: {product_info['name']}")
    print(f"\n price: ${product_info['price']:.2f}")
    print(f"\n category: {product_info['category']}")
    print(f"\n stock: {product_info['stock']}")

total_inventory_value=sum(prod["price"] * prod["stock"] for prod in products.values())  
print(total_inventory_value)
#Calculate total inventory value (price * stock for all products)    

#Find products with stock < 10

result = [
    f"{pid} - {info['name']}"
    for pid, info in products.items()
    if info["stock"] < 10
]

print(f"Low stock products: [{', '.join(result)}]")

#Find the most expensive product
most_expensive = max(products.values(), key=lambda x: x["price"])
print(f"Most expensive: {most_expensive['name']} at ${most_expensive['price']}")

#Group products by category (return a dict mapping category to list of product names)
category_map = {}

for pid, info in products.items():
    category = info["category"]
    name = info["name"]
    
    if category not in category_map:
        category_map[category] = []
    
    category_map[category].append(name)

print(category_map)