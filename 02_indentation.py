age =25
if age> 20:
  print("adult")
  print("can vote")
else:
    print("minor")
    print("cannot vote")     
    
salary = 75000

if salary>=5000:
    print("Good salary")
    if salary>=10000:
        print("excellant salary") 
    else:
        print("room grow")
        
else:
    print("entry level salary")   
    
    
score = 85

if score>=90:
    grade="A"
elif score>80:
     grade="B"
elif score>70:
     grade="C"
elif score > 60:
     grade="D"
elif score >50:
     grade="E"
else:
     grade="A"     
     
print(f"score {score}, grade{grade}") 

is_manager="true"
years_experience =5

if is_manager and  years_experience>= 3:
    print("eligible for senior management")
elif is_manager or years_experience >=10:
  print("eligible for promotion consideration")
else:
    print("not eligible yet")   
          
    