print("\n" + "="*70)
print("PROGRAM 7: DICTIONARY COMPREHENSIONS (Advanced)")
print("="*70)
numbers = [1, 2, 3, 4, 5]

squares = {num: num**2 for num in numbers}
print(squares)
#Filter while building
even_squares = {num: num**2 for num in numbers if num % 2 == 0}
print(even_squares)
prices = {"apple": 1.00, "banana": 0.50, "orange": 0.75}
discounted = {fruit: price * 0.9 for fruit, price in prices.items()}
print(discounted)
original = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original.items()}
print(f"Swapped: {swapped}")
numbers = range(1, 11)
parity = {num: "even" if num % 2 == 0 else "odd" for num in numbers}
print(f"Parity: {parity}")

names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [95, 78, 88, 92, 85]
#Create dict with only students who scored >= 85

high_scorers = {score for score in scores if score >=85}
print(high_scorers)
letter_grades = {score: "A" if score >= 90 else
                 "B" if score >= 80 else
                 "C" if score >= 70 else
                 "F" for score in scores}
print(letter_grades)
#Create dict mapping names to name length
even_squares = {num: num**2 for num in numbers if num % 2 == 0}
name_lengths = {name: len(name) for name in names}
print(name_lengths)
#Given dict {1: 10, 2: 20, 3: 30, 4: 40}, create dict with doubled values
original = {1: 10, 2: 20, 3: 30, 4: 40}
doubled = {value: value*2 for key, value in original.items()}
print(doubled)