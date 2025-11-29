# TODO: Check if an employee is eligible for promotion
# Rules:
# - Years of service >= 3
#   - If performance_score >= 8: "Eligible for senior promotion"
#   - If performance_score >= 6: "Eligible for standard promotion"
#   - Else: "Not eligible yet - improve performance"
# - Years of service < 3: "Too early for promotion"

years_of_experience=5
performance_score=7
salary=45000


if years_of_experience>=3:
    if performance_score >= 8:
        print("Eligible for senior promotion")
    elif performance_score >= 8:
        print("Eligible for standard promotion")
    else:
        print("Not eligible yet - improve performance")
else:
    print("Too early for promotion")
        
        