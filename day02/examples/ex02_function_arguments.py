"""
================================================================================
CodeArena Day 2 - Example 2: Function Arguments
================================================================================
"""

# Example 2: Different Types of Function Arguments

# 1. POSITIONAL ARGUMENTS
# Position se value assign hoti hai
def register_player(name, email, age):
    """
    Positional arguments - order important hai
    """
    print(f"Registered: {name}, {email}, {age} years")

register_player("Rahul", "rahul@email.com", 22)
# Output: Registered: Rahul, rahul@email.com, 22 years


# 2. KEYWORD ARGUMENTS
# Naam batake value do, order matter nahi karta
def update_score(player_id, points, match_id):
    """
    Keyword arguments - naam se value do
    """
    print(f"Player {player_id} got {points} points in match {match_id}")

# Order alag hai but naam se pata chal raha hai
update_score(points=100, match_id=5, player_id=101)
# Output: Player 101 got 100 points in match 5


# 3. DEFAULT PARAMETER VALUES
# Agar value na do toh default use hoga
def create_badge(player_name, badge_type="Bronze", xp_bonus=50):
    """
    Default values - agar parameter na dein toh yeh use hoga
    """
    print(f"\n{badge_type} Badge awarded to {player_name}")
    print(f"XP Bonus: +{xp_bonus} points")

# Sirf required argument do
print("\n--- With defaults ---")
create_badge("Amit")

# Kuch override karo
print("\n--- Override one default ---")
create_badge("Priya", badge_type="Silver")

# Sab override karo
print("\n--- Override all ---")
create_badge("Rahul", "Gold", 200)


# 4. ARBITRARY ARGUMENTS (*args)
# Kitne bhi arguments le sakte ho
def calculate_total(*scores):
    """
    *scores - jitne bhi arguments do, sabko tuple mein le lega
    """
    print(f"\nReceived scores: {scores}")  # Tuple dikhega
    print(f"Number of matches: {len(scores)}")
    
    total = 0
    for score in scores:
        total += score  # Sab scores add karo
    
    average = total / len(scores) if scores else 0
    return total, average

# Different number of arguments
total1, avg1 = calculate_total(100, 150, 200)
print(f"Total: {total1}, Average: {avg1}")

total2, avg2 = calculate_total(50, 75, 100, 125, 150, 175)
print(f"Total: {total2}, Average: {avg2}")


# 5. ARBITRARY KEYWORD ARGUMENTS (**kwargs)
# Kitne bhi keyword arguments le sakte ho
def create_player_profile(**details):
    """
    **details - jitne bhi keyword arguments, sab dictionary mein
    """
    print(f"\nPlayer Profile:")
    print(f"Total fields: {len(details)}")
    
    for key, value in details.items():
        print(f"  {key}: {value}")
    
    return details

# Different fields ke saath
profile1 = create_player_profile(
    name="Rahul",
    age=22,
    level=5,
    xp=3000
)

profile2 = create_player_profile(
    name="Sonia",
    email="sonia@game.com",
    country="India",
    rank="Gold",
    matches_played=50
)


# 6. MIXING ALL TYPES
# Sab types ek saath use kar sakte ho
def tournament_result(player_name, tournament_id, *scores, status="completed", **details):
    """
    Mixed arguments:
    - player_name: required positional
    - tournament_id: required positional
    - *scores: arbitrary positional (kitne bhi scores)
    - status: default value
    - **details: arbitrary keyword arguments
    """
    print(f"\n{'='*50}")
    print(f"Player: {player_name}")
    print(f"Tournament ID: {tournament_id}")
    print(f"Status: {status}")
    
    if scores:
        print(f"Scores: {scores}")
        print(f"Total: {sum(scores)}")
    
    if details:
        print("Additional Details:")
        for key, value in details.items():
            print(f"  {key}: {value}")
    print(f"{'='*50}")

# Mix sab types
tournament_result(
    "Amit",              # positional
    101,                 # positional
    100, 150, 200, 175,  # *args
    status="active",     # keyword with default
    rank="Silver",       # **kwargs
    country="India",
    matches_won=4
)
