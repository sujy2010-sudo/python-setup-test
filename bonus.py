# 02_exercise.py
"""
YOUR TURN! Write nested if statements
"""

# TODO: Check if an employee is eligible for promotion
# Rules:
# - Years of service >= 3
#   - If performance_score >= 8: "Eligible for senior promotion"
#   - If performance_score >= 6: "Eligible for standard promotion"
#   - Else: "Not eligible yet - improve performance"
# - Years of service < 3: "Too early for promotion"

years_of_service = 1
performance_score = 7
salary = 45000
# Write your code here:



if years_of_service >= 3 and performance_score >=8:
  print("Eligible for senior promotion")
if years_of_service >= 3 and performance_score >=6:
  print("Eligible for standard promotion")
if years_of_service <3:
    print("Too early for promotion")
if salary <50000:
    print("Review salary first")


# BONUS: Add another condition - if salary < 50000, add "Review salary first"


# Write bonus code here: