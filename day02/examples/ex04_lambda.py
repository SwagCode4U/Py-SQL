"""
================================================================================
CodeArena Day 2 - Example 4: Lambda Functions
================================================================================
"""

# Example 4: Lambda Functions (Anonymous Functions)
# Lambda ek chhota, anonymous function hota hai
# Ek line mein function likh sakte ho


# 1. BASIC LAMBDA
# Normal function:
def square_normal(x):
    return x ** 2

# Lambda version:
square_lambda = lambda x: x ** 2

# Dono same kaam karte hain
print("Normal function:", square_normal(5))      # 25
print("Lambda function:", square_lambda(5))       # 25


# 2. LAMBDA WITH MULTIPLE PARAMETERS
calculate_xp = lambda base, bonus, matches: base + (bonus * matches)

result = calculate_xp(1000, 50, 10)
print(f"\nTotal XP: {result}")  # 1000 + (50 * 10) = 1500


# 3. LAMBDA WITH DEFAULT VALUES
get_status = lambda level, is_active=True: f"Level {level} - {'Active' if is_active else 'Inactive'}"

print(f"\n{get_status(5)}")           # Default active
print(f"{get_status(3, False)}")      # Explicit inactive


# 4. LAMBDA WITH CONDITIONS
check_rank = lambda xp: "Gold" if xp >= 5000 else "Silver" if xp >= 2500 else "Bronze"

print("\n--- Rank Check ---")
for xp in [1000, 3000, 7500]:
    print(f"XP {xp}: {check_rank(xp)} Rank")


# 5. USING LAMBDA WITH SORTING
players = [
    {"name": "Rahul", "xp": 3000},
    {"name": "Priya", "xp": 7500},
    {"name": "Amit", "xp": 1500},
    {"name": "Sonia", "xp": 5000}
]

# XP ke hisaab se sort karo (descending)
# key parameter mein lambda do
sorted_players = sorted(players, key=lambda p: p["xp"], reverse=True)

print("\n--- Players Sorted by XP ---")
for i, player in enumerate(sorted_players, 1):
    print(f"{i}. {player['name']}: {player['xp']} XP")


# 6. LAMBDA WITH FILTER()
# filter() mein use karte hain
scores = [50, 150, 200, 75, 300, 125, 80]

# 100 se zyada wale scores filter karo
high_scores = list(filter(lambda x: x >= 100, scores))

print(f"\nAll scores: {scores}")
print(f"High scores (>=100): {high_scores}")


# 7. LAMBDA WITH MAP()
# map() mein use karte hain
xp_list = [1000, 2000, 3000, 4000]

# Sab XP ko 1.5 se multiply karo (bonus)
boosted_xp = list(map(lambda x: int(x * 1.5), xp_list))

print(f"\nOriginal XP: {xp_list}")
print(f"Boosted XP: {boosted_xp}")


# 8. LAMBDA WITH REDUCE()
from functools import reduce

match_scores = [100, 150, 200, 120, 180]

# Saare scores ka total nikalo
total_score = reduce(lambda x, y: x + y, match_scores)

print(f"\nMatch scores: {match_scores}")
print(f"Total: {total_score}")

# Maximum score nikalo
max_score = reduce(lambda x, y: x if x > y else y, match_scores)
print(f"Highest score: {max_score}")


# 9. PRACTICAL EXAMPLE: Leaderboard Formatter
format_entry = lambda rank, name, score: f"#{rank:<3} {name:<10} {score:>6} pts"

print("\n--- Leaderboard ---")
print("-" * 30)
print(format_entry(1, "Priya", 7500))
print(format_entry(2, "Sonia", 5000))
print(format_entry(3, "Rahul", 3000))
print(format_entry(4, "Amit", 1500))


# 10. WHEN TO USE LAMBDA VS NORMAL FUNCTION
print("\n" + "=" * 60)
print("Lambda use karo jab:")
print("  ✓ Chhota, one-time use function chahiye")
print("  ✓ sorted(), map(), filter() ke saath")
print("  ✓ Code concise rakhna ho")
print("\nNormal function use karo jab:")
print("  ✓ Complex logic hai")
print("  ✓ Multiple lines ki zaroorat hai")
print("  ✓ Reuse karna hai baar baar")
print("  ✓ Documentation chahiye")
print("=" * 60)
