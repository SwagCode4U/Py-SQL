"""
================================================================================
CodeArena Day 1 - Example 1: Variables and Data Types
================================================================================
"""

# Example 1: Player Profile Variables
# Is example mein hum basic variables sikhte hain

# STRING variable - text store karne ke liye
# player_name mein player ka naam store hoga
player_name = "Rahul"                      # Rahul player ka naam

# INTEGER variable - whole numbers ke liye
# player_age mein player ki age store hogi
player_age = 22                            # 22 saal ki age

# FLOAT variable - decimal numbers ke liye
# player_xp mein experience points store honge
player_xp = 1500.5                         # 1500.5 XP points

# BOOLEAN variable - True/False values ke liye
# is_active batata hai ki player active hai ya nahi
is_active = True                           # True matlab active hai

# Sab values print karo
print("=== Player Profile ===")           # Heading print karo
print(f"Naam: {player_name}")             # f-string se naam print
print(f"Age: {player_age} saal")          # Age print karo
print(f"XP Points: {player_xp}")          # XP points print
print(f"Active Status: {is_active}")      # Status print

# type() function se check karo ki variable ka type kya hai
print(f"\nplayer_name ka type: {type(player_name)}")  # <class 'str'>
print(f"player_age ka type: {type(player_age)}")       # <class 'int'>
print(f"player_xp ka type: {type(player_xp)}")         # <class 'float'>
print(f"is_active ka type: {type(is_active)}")         # <class 'bool'>

# Output:
# === Player Profile ===
# Naam: Rahul
# Age: 22 saal
# XP Points: 1500.5
# Active Status: True
