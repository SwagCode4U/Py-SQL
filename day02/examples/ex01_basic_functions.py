"""
================================================================================
CodeArena Day 2 - Example 1: Basic Functions
================================================================================
"""

# Example 1: Simple Function Definition
# Function ek block of code hai jo specific kaam karta hai

# Function 1: Simple greeting
# def keyword se function define karte hain
def say_hello():
    """
    Yeh function sirf 'Hello' print karta hai
    """
    print("Hello CodeArena Player!")  # Jab function call karo tab yeh print hoga

# Function ko call karo
say_hello()  # Output: Hello CodeArena Player!


# Function 2: Function with parameter (input leta hai)
def greet_player(player_name):
    """
    Yeh function player ka naam leke greeting deta hai
    Parameter: player_name - jisko greet karna hai
    """
    print(f"Welcome to CodeArena, {player_name}!")

# Function call with argument
greet_player("Rahul")      # Output: Welcome to CodeArena, Rahul!
greet_player("Priya")      # Output: Welcome to CodeArena, Priya!


# Function 3: Function with multiple parameters
def calculate_xp(base_xp, bonus_xp, matches):
    """
    Total XP calculate karta hai
    Parameters:
        base_xp - starting XP
        bonus_xp - bonus per match
        matches - kitne matches khele
    """
    total = base_xp + (bonus_xp * matches)
    return total  # return se value wapas bhejte hain

# Function se value receive karo
my_xp = calculate_xp(1000, 50, 10)
print(f"\nTotal XP earned: {my_xp}")  # 1000 + (50 * 10) = 1500


# Function 4: Function with default parameters
def create_player(username, level=1, xp=0):
    """
    Player profile create karta hai
    Default values: level=1, xp=0 (agar user na de toh)
    """
    print(f"\nPlayer Created:")
    print(f"  Username: {username}")
    print(f"  Level: {level}")
    print(f"  XP: {xp}")
    return {"username": username, "level": level, "xp": xp}

# Default values ke saath
player1 = create_player("Amit")

# Custom values ke saath
player2 = create_player("Sonia", level=5, xp=2500)


# Function 5: Function jo multiple values return karta hai
def get_player_stats():
    """
    Player ke stats return karta hai
    Multiple values tuple ki form mein return hoti hain
    """
    level = 10
    xp = 5000
    rank = "Gold"
    return level, xp, rank  # 3 values return ho rahi hain

# Multiple values receive karo
player_level, player_xp, player_rank = get_player_stats()
print(f"\nPlayer Stats:")
print(f"  Level: {player_level}")
print(f"  XP: {player_xp}")
print(f"  Rank: {player_rank}")

print("\n" + "=" * 50)
print("Functions ka use se code reusable aur organized hota hai!")
print("=" * 50)
