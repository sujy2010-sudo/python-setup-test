print("\n" + "="*70)
print("PROGRAM 4: BUILDING DICTIONARIES - COUNTING PATTERN")
print("="*70)
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

word_counts={}
for word in words:
    word_counts[word]=word_counts.get(word,0)+ 1

for  word,counts in word_counts.items():
    print(f"{word}:{counts}")  
    
text = "hello world"
letter_counts = {}

for letter in text:
    if letter != ' ':
        letter_counts[text]=letter_counts.get(text,0)+1
for letter,count in  letter_counts.items():
    print(f"{letter}:{count}")       
    
    
departments = ["Engineering", "Sales", "Engineering", "HR", "Sales",
               "Engineering", "Marketing", "Sales"]

statuses = ["active", "inactive", "active", "active", "inactive",
            "pending", "active", "inactive"]

grade_list = ["A", "B", "A", "C", "B", "A", "A", "B", "C", "A"]

#1. Count how many times each department appears                 
dept_counts = {}

for dept in departments:
    dept_counts[dept]=dept_counts.get(dept,0)+1
    
for  dept,counts in dept_counts.items():
    print(f"{dept}:{counts}")      

#2. Count how many times each status appears
#3. Count grades (how many A's, B's, C's etc)
status_counts = {}
# TODO: Count statuses

for status in statuses:
    status_counts[status]=status_counts.get(status,0)+1
for status_name,count in  status_counts.items():
    print(f"{status_name}:{count}")  
grade_counts = {}             

grade_list
for grade in  grade_list:
    grade_counts[grade]=grade_counts.get(grade,0)+1
for grade_Value,count in grade_counts.items():
     print(f"{grade_Value}:{count}")             