"""
================================================================================
CodeArena Day 1 - Example 4: User Input and Basic Output
================================================================================
"""

# Example 4: Player Registration Form
# Is example mein hum user se input lena sikhte hain

print("=" * 50)
print("   CodeArena - Player Registration")
print("=" * 50)

# 1. Basic input - user se naam lena
# input() function user se text input leti hai
player_name = input("\nApna naam daalo: ")              # User se naam poochho
print(f"Swagat hai, {player_name}!")                    # Welcome message

# 2. Input with type conversion (int)
# By default input() string return karti hai
# Integer chahiye toh int() mein convert karo
age_input = input("Apni age daalo: ")                   # Age input as string
player_age = int(age_input)                             # String ko integer mein convert
print(f"Aapki age {player_age} saal hai")              # Print karo

# 3. Input with type conversion (float)
xp_input = input("Current XP kitne hain? ")            # XP as string
player_xp = float(xp_input)                             # String ko float mein convert
print(f"Aapke paas {player_xp} XP points hain")        # Print karo

# 4. Boolean input (yes/no)
active_input = input("Kya aap active player ho? (yes/no): ")  # Yes/No poochho
is_active = active_input.lower() == "yes"               # Compare karke boolean banao
print(f"Active status: {is_active}")                    # True ya False print karo

# 5. Multiple inputs in one line
# split() function se ek line mein multiple values le sakte hain
print("\n--- Ek line mein 3 skills daalo (comma se separate karo) ---")
skills_input = input("Skills (jaise: Python, SQL, Java): ")  # Comma separated
skills_list = skills_input.split(",")                   # Comma se split karo
print(f"Aapki skills: {skills_list}")

# 6. Registration summary
print("\n" + "=" * 50)
print("   Registration Summary")
print("=" * 50)

# Saari info ek saath print karo
print(f"Player Name: {player_name}")
print(f"Age: {player_age} years")
print(f"Current XP: {player_xp}")
print(f"Active Status: {'Yes' if is_active else 'No'}")
print(f"Skills: {', '.join(skills_list)}")               # List ko string mein convert

# 7. Calculations with user input
print("\n--- XP Calculator ---")
matches_won = int(input("Kitne matches jeete? "))       # Integer input
xp_per_match = int(input("Har match mein kitne XP mile? "))  # Integer input
total_xp_earned = matches_won * xp_per_match            # Multiply karo

print(f"\nTotal XP Earned: {total_xp_earned}")
print(f"Previous XP: {player_xp}")
print(f"New Total XP: {player_xp + total_xp_earned}")

# 8. Formatted output
print("\n" + "-" * 50)
print("Registration Complete!")
print("-" * 50)
print(f"{'Player:':<20} {player_name}")                  # Left align 20 chars
print(f"{'Level:':<20} {'Beginner'}")                    # Static text
print(f"{'Total XP:':<20} {player_xp + total_xp_earned}")
print("-" * 50)

# Note: Jab aap is program ko run karoge,
# tab input() function rokega aur aap se value maangega
# Terminal mein type karke ENTER press karo
