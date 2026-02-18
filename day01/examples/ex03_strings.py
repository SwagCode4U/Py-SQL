"""
================================================================================
CodeArena Day 1 - Example 3: String Operations and Formatting
================================================================================
"""

# Example 3: Player Welcome Messages
# Is example mein hum strings ke saath operations sikhte hain

# 1. String creation using single quotes
welcome_msg = 'CodeArena mein aapka swagat hai!'  # Welcome message

# 2. String creation using double quotes
tournament_name = "Python Championship 2024"       # Tournament name

# 3. String creation using triple quotes (multi-line)
rules = """
Tournament Rules:
1. Har match mein fair khelo
2. Cheating allowed nahi hai
3. XP points jeetne par milenge
4. Level up hone par rewards milenge
"""

print("=== Welcome Message ===")
print(welcome_msg)
print(f"\nTournament: {tournament_name}")
print(rules)

# 4. String Concatenation (+ operator se strings join karna)
first_name = "Amit"
last_name = "Sharma"
full_name = first_name + " " + last_name        # Do strings ko joda
print(f"\nFull Name: {full_name}")

# 5. String Repetition (* operator se string repeat karna)
star_pattern = "*" * 30                          # 30 stars
print(f"\n{star_pattern}")

# 6. String Length (len() function)
# String mein kitne characters hain
name_length = len(full_name)                     # Amit Sharma = 11 characters
print(f"Name ki length: {name_length} characters")

# 7. String Indexing (individual characters access karna)
# Python mein indexing 0 se start hoti hai
first_char = full_name[0]                        # 0 index = 'A'
last_char = full_name[-1]                        # -1 index = last character
print(f"\nPehla character: {first_char}")
print(f"Aakhri character: {last_char}")

# 8. String Slicing (substring nikaalna)
# [start:end] - start se lekar end-1 tak
first_4_chars = full_name[0:4]                   # Amit
last_5_chars = full_name[-5:]                    # Sharma
print(f"\nPehle 4 characters: {first_4_chars}")
print(f"Aakhri 5 characters: {last_5_chars}")

# 9. String Methods (built-in functions)
upper_name = full_name.upper()                   # AMIT SHARMA
lower_name = full_name.lower()                   # amit sharma
title_name = full_name.title()                   # Amit Sharma
print(f"\nUPPERCASE: {upper_name}")
print(f"lowercase: {lower_name}")
print(f"Title Case: {title_name}")

# 10. f-strings (formatted strings) - sabse best tarika
player = "Rahul"
xp = 2500
level = 5

# f-string mein variables directly curly braces mein daal sakte hain
status_message = f"Player {player} ka Level {level} hai aur {xp} XP points hain!"
print(f"\n{status_message}")

# f-strings mein calculations bhi kar sakte hain
next_level_xp = xp + 500
future_message = f"Next level ke liye {next_level_xp} XP chahiye"
print(future_message)

# 11. String replacement
old_message = "Welcome to Tournament"
new_message = old_message.replace("Tournament", "CodeArena")  # Replace kiya
print(f"\nOriginal: {old_message}")
print(f"Modified: {new_message}")

# 12. String splitting
player_data = "Rahul,25,Level5,2500XP"          # CSV format mein data
player_list = player_data.split(",")            # Comma se split kiya
print(f"\nSplit result: {player_list}")
print(f"Player ka naam: {player_list[0]}")
print(f"Player ki age: {player_list[1]}")
