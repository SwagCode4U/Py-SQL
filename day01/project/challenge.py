"""
================================================================================
CodeArena Day 1 - Challenge: Test Your Learning
================================================================================

Challenge 1: Variable Swap
Do variables ke values ko bina third variable ke swap karo
Hint: Python mein a, b = b, a use kar sakte ho

Challenge 2: Area Calculator
User se circle ka radius lo aur area calculate karo
Formula: area = 3.14 * radius * radius

Challenge 3: String Reversal
User se ek string lo aur usko reverse karo
Hint: slicing use karo [::-1]

Challenge 4: Temperature Converter
Celsius ko Fahrenheit mein convert karo
Formula: fahrenheit = (celsius * 9/5) + 32

================================================================================
SOLUTIONS:
================================================================================
"""

print("=" * 60)
print("   CodeArena Day 1 - Challenges")
print("=" * 60)

# CHALLENGE 1: Variable Swap
print("\n" + "-" * 60)
print("CHALLENGE 1: Variable Swap")
print("-" * 60)

x = 10
y = 20
print(f"Pehle: x = {x}, y = {y}")

# Python magic - tuple unpacking se swap
x, y = y, x
print(f"Baad mein: x = {x}, y = {y}")
print("✓ Values swap ho gayi!")

# CHALLENGE 2: Area Calculator
print("\n" + "-" * 60)
print("CHALLENGE 2: Circle Area Calculator")
print("-" * 60)

radius = 5.0
pi = 3.14159
area = pi * radius ** 2  # radius ki power 2
print(f"Radius: {radius}")
print(f"Area: {area}")

# CHALLENGE 3: String Reversal
print("\n" + "-" * 60)
print("CHALLENGE 3: String Reversal")
print("-" * 60)

text = "CodeArena"
reversed_text = text[::-1]  # [::-1] se string reverse hoti hai
print(f"Original: {text}")
print(f"Reversed: {reversed_text}")

# CHALLENGE 4: Temperature Converter
print("\n" + "-" * 60)
print("CHALLENGE 4: Temperature Converter")
print("-" * 60)

celsius = 30
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

print("\n" + "=" * 60)
print("   Challenges Complete! Great Job!")
print("=" * 60)

"""
================================================================================
WHAT YOU LEARNED TODAY:
================================================================================

Python Basics:
✓ Variables aur Data Types (str, int, float, bool)
✓ Arithmetic Operations (+, -, *, /, //, %, **)
✓ String Operations (concatenation, slicing, methods)
✓ User Input aur Output
✓ f-strings for formatting

MySQL Basics:
✓ Database creation
✓ Table creation with constraints
✓ Data types in MySQL
✓ Primary Key aur Foreign Key
✓ Relationships between tables

Key Concepts:
✓ Python mein code kaise likhte hain
✓ Comments kaise likhte hain
✓ MySQL mein database kaise create karte hain
✓ Tables ka structure kaise design karte hain

Tomorrow: Day 2 - Functions aur INSERT queries
================================================================================
"""
