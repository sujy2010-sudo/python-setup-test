names =["alice","bob","charlie"]

print(names[0])
print(names[-1])
print(names[-2])
print(names[0:2])
print(names[1:])
print(names[:2])

names.append("david")
print(names)
names.insert(1,"eve")
print(names)
names.remove("eve")
print(names)


last_name =names.pop()
print(f"removed:{last_name}")
print(names)

if "alice" in names:
    print("alice in names list")
print(f"total names:{len(names)}")


print("\n---simple loop---")

for name in names:
    print(f"hello {name}")
    
    
print("\n-- loop with index---") 

for index,name in enumerate(names):
    print(f"hello{index+1}.{name}")   
long_names=[name for name in names if len(names)>2]
print(f"long name :{long_names}")   

upper_long_names=[name.upper() for name in names if len(names)>2] 
print(f"upper long names{upper_long_names}")


employee_ids=[101,102,103,104,105]
print(employee_ids)

double_ids=[id*2 for id in employee_ids ]

print(f"\n double ids{double_ids}")

high_ids=[id for id in employee_ids if id >102]

print(f"high id{high_ids}")

formattedid=[f"EMP{id:05d}" for id in employee_ids]

print(f"\nformatted ids {formattedid}")



departments=[["alice","bob"],
             ["charlie","angle"],
             ["eve"]]

all_employees=[emp for dept in departments for emp in dept]

print(f"{all_employees}")

print("\n using range")
for i in range(5):
    print(i,end=" ")
print()


for i in range(0,10,2):
    print(i,end=" ")
print()

numbers=list(range(1,11))
print(f"\n numbers range 1..10:{numbers}")    

print(f"sum{sum(numbers)}")
print(f"min{min(numbers)}")
print(f"max{max(numbers)}")
print(f"average{sum(numbers)/len(numbers)}")