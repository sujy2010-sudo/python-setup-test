# 02_indentation.py
"""Understanding Python's indentation rules
This is THE most important difference from Java!
"""

# 🔴 JAVA:
# if (age >= 18) {
#     System.out.println("Adult");
# } else {
#     System.out.println("Minor");
# }

# 🐍 PYTHON - No braces, use indentation!
age = 25

if age >= 18:
    print("Adult")  # 4 spaces or 1 tab (be consistent!)
    print("Can vote")
else:
    print("Minor")
    print("Cannot vote")

# ⚠️ COMMON MISTAKE - Wrong indentation will cause IndentationError
# VS Code will help you avoid this!

# Nested conditions
salary = 75000

if salary >= 50000:
    print("Good salary!")
    if salary >= 100000:
        print("Excellent salary!")  # Double indentation (8 spaces)
    else:
        print("Room to grow")
else:
    print("Entry level salary")

# Multiple conditions with elif
score = 90

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Compound conditions (like Java's && and ||)
is_manager = True
years_experience = 5

if is_manager and years_experience >= 3:
    print("Eligible for senior management")
elif is_manager or years_experience >= 10:
    print("Eligible for promotion consideration")
else:
    print("Not eligible yet")
