print("--Basic while loop")
count =0

while count <5:
    print (f"count{count}")
    count +=1
     
    
print("\n --Break example--")
numbers= [1,2,3,4,5,6,7,8,9,0]

for num in numbers:
    if num == 6:
        break 
    print(num,end=" ")
print()

print("\n find first error") 
log_levels=["INFO","WARNING","INFO","DEBUG","CRITICAL"]

for index,level in enumerate(log_levels):
    if level =="ERROR":
        print(f"first error found at position{index}")
        break
        print(f"Position{index}:{level}-Ok")
        
print("\n while with break")
attempts=0
max_attempts=3

while attempts<max_attempts:
    print(f"Attempt{attempts+1}")
    
    if attempts==1:
        print("success")
        break
    attempts+=1
else:
    print("all attempts failed")

search_list=[1,2,3,4,5]
search_value=6    
    
for num in search_list:
    if num == search_value:
        print(f"found in {search_value}")    
        break
    else:
        print(f"{search_value} not found in list")
        
print("\n nested loops")
departments=["engineering","sales","HR"]
positions=["juniors","senior"]
for dept in departments:
    for position in positions:
        print(f"{position}{dept}developer")                   
        
       