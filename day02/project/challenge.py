"""
================================================================================
CodeArena Day 2 - Challenge: Practice Functions
================================================================================

Challenge 1: XP Calculator Function
Ek function banao jo player ke matches ke XP calculate kare
Input: base_xp, matches (list of scores)
Output: total_xp, average_xp

Challenge 2: Level Up Checker
Function banao jo check kare ki player level up hue ya nahi
Input: current_xp, required_xp
Output: True/False, remaining_xp

Challenge 3: Tournament Registration
Function banao jo tournament mein player register kare
Validation check kare: age >= 13, email valid

Challenge 4: Lambda Leaderboard
Lambda function use karke players ko XP ke hisaab se sort karo
================================================================================
"""

print("=" * 60)
print("   CodeArena Day 2 - Challenges")
print("=" * 60)


# CHALLENGE 1: XP Calculator
print("\n" + "-" * 60)
print("CHALLENGE 1: XP Calculator")
print("-" * 60)

def calculate_player_xp(base_xp, match_scores):
    """
    Player ka total aur average XP calculate karta hai
    """
    total_match_xp = sum(match_scores)  # Sab scores add karo
    total_xp = base_xp + total_match_xp
    average_xp = total_match_xp / len(match_scores) if match_scores else 0
    
    return total_xp, average_xp

# Test
base = 1000
scores = [150, 200, 175, 225, 100]
total, average = calculate_player_xp(base, scores)
print(f"Base XP: {base}")
print(f"Match Scores: {scores}")
print(f"Total XP: {total}")
print(f"Average per match: {average:.2f}")


# CHALLENGE 2: Level Up Checker
print("\n" + "-" * 60)
print("CHALLENGE 2: Level Up Checker")
print("-" * 60)

def check_level_up(current_xp, required_xp):
    """
    Check karta hai ki level up ho sakta hai ya nahi
    """
    if current_xp >= required_xp:
        return True, 0  # Level up possible, no XP remaining needed
    else:
        remaining = required_xp - current_xp
        return False, remaining

# Test
for current, required in [(800, 1000), (1500, 1000), (2500, 3000)]:
    can_level_up, remaining = check_level_up(current, required)
    status = "✓ Level UP!" if can_level_up else f"✗ Need {remaining} more XP"
    print(f"Current: {current}, Required: {required} -> {status}")


# CHALLENGE 3: Tournament Registration
print("\n" + "-" * 60)
print("CHALLENGE 3: Tournament Registration")
print("-" * 60)

def register_for_tournament(name, age, email, tournament):
    """
    Tournament registration with validation
    """
    # Age check
    if age < 13:
        return False, "Age must be 13 or above"
    
    # Email validation (basic)
    if "@" not in email or "." not in email.split("@")[-1]:
        return False, "Invalid email format"
    
    # Success
    return True, f"✓ {name} registered for {tournament}"

# Test cases
test_registrations = [
    ("Rahul", 20, "rahul@email.com", "Python Cup"),
    ("Kid", 10, "kid@email.com", "Python Cup"),
    ("Invalid", 25, "invalid-email", "SQL Masters")
]

for name, age, email, tour in test_registrations:
    success, message = register_for_tournament(name, age, email, tour)
    print(f"{name}: {message}")


# CHALLENGE 4: Lambda Leaderboard
print("\n" + "-" * 60)
print("CHALLENGE 4: Lambda Leaderboard")
print("-" * 60)

players = [
    {"name": "Rahul", "xp": 2500, "matches": 25},
    {"name": "Priya", "xp": 5200, "matches": 40},
    {"name": "Amit", "xp": 1800, "matches": 15},
    {"name": "Sonia", "xp": 3900, "matches": 32}
]

# Sort by XP (descending)
sorted_by_xp = sorted(players, key=lambda p: p["xp"], reverse=True)
print("\nBy XP (High to Low):")
for i, p in enumerate(sorted_by_xp, 1):
    print(f"  {i}. {p['name']}: {p['xp']} XP")

# Sort by matches played
sorted_by_matches = sorted(players, key=lambda p: p["matches"], reverse=True)
print("\nBy Matches Played:")
for i, p in enumerate(sorted_by_matches, 1):
    print(f"  {i}. {p['name']}: {p['matches']} matches")

# Sort by XP per match (efficiency)
sorted_by_efficiency = sorted(
    players, 
    key=lambda p: p["xp"] / p["matches"], 
    reverse=True
)
print("\nBy Efficiency (XP per Match):")
for i, p in enumerate(sorted_by_efficiency, 1):
    efficiency = p["xp"] / p["matches"]
    print(f"  {i}. {p['name']}: {efficiency:.1f} XP/match")


print("\n" + "=" * 60)
print("   Challenges Complete! Great Job!")
print("=" * 60)

"""
================================================================================
WHAT YOU LEARNED TODAY:
================================================================================

Python Functions:
✓ def keyword se function create karna
✓ Parameters aur arguments
✓ Return values (single, multiple, None)
✓ Default parameter values
✓ *args (arbitrary positional arguments)
✓ **kwargs (arbitrary keyword arguments)
✓ Lambda functions
✓ Variable scope (global, local, nonlocal)
✓ Docstrings for documentation

MySQL INSERT:
✓ INSERT INTO single row
✓ executemany() for bulk operations
✓ %s placeholders for security
✓ cursor.lastrowid for last insert ID
✓ connection.commit() to save changes
✓ Foreign key relationships

Best Practices:
✓ Functions ko small aur focused rakho
✓ Reusable database connection function
✓ Error handling with try-except
✓ Proper resource cleanup (cursor.close(), connection.close())

Tomorrow: Day 3 - Modules aur proper project structure
================================================================================
"""
