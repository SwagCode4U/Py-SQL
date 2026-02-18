"""
================================================================================
CodeArena Day 2 - Example 3: Scope and Return Values
================================================================================
"""

# Example 3: Variable Scope aur Return Values

# GLOBAL VARIABLE
# Function ke bahar define hota hai, pure program mein accessible
arena_name = "CodeArena"  # Global variable


def show_global():
    """
    Global variable ko function ke andar read kar sakte hain
    """
    print(f"Global arena: {arena_name}")  # Global variable access

show_global()  # CodeArena print hoga


def try_modify_global():
    """
    Agar directly modify karne ki koshish karo toh error aayega
    ya local variable ban jayega
    """
    arena_name = "NewArena"  # Yeh local variable ban gaya!
    print(f"Inside function: {arena_name}")  # NewArena

try_modify_global()
print(f"Outside function: {arena_name}")  # CodeArena (unchanged!)


def modify_global():
    """
    Global variable modify karne ke liye 'global' keyword use karo
    """
    global arena_name  # Batao ki global variable use kar rahe hain
    arena_name = "CodeArena Pro"  # Ab global variable change hoga
    print(f"Modified inside: {arena_name}")

modify_global()
print(f"Outside after modify: {arena_name}")  # CodeArena Pro


# LOCAL VARIABLES
# Function ke andar define hote hain, bahar accessible nahi
def create_match():
    """
    Local variables sirf is function ke andar kaam karte hain
    """
    match_id = 1001  # Local variable
    player1 = "Rahul"  # Local variable
    player2 = "Amit"  # Local variable
    
    print(f"\nMatch {match_id}: {player1} vs {player2}")
    return match_id

match = create_match()
print(f"Returned match ID: {match}")
# print(player1)  # ERROR! player1 local variable hai, bahar accessible nahi


# RETURN MULTIPLE VALUES
def get_player_data(player_id):
    """
    Dictionary return karna - complex data bhej sakte ho
    """
    # Database se fetch karne jaise simulate karte hain
    data = {
        "id": player_id,
        "name": f"Player_{player_id}",
        "level": 5,
        "xp": 2500,
        "rank": "Gold"
    }
    return data

player = get_player_data(101)
print(f"\nPlayer Data: {player}")
print(f"Name: {player['name']}")
print(f"Level: {player['level']}")


# RETURN LIST
def get_top_players():
    """
    List return karna - multiple items bhej sakte ho
    """
    top_players = ["Rahul", "Priya", "Amit", "Sonia", "Vikram"]
    return top_players

players = get_top_players()
print(f"\nTop Players: {players}")
for i, p in enumerate(players, 1):
    print(f"  {i}. {p}")


# RETURN WITH CONDITIONS
def check_level(xp):
    """
    Different values return based on conditions
    """
    if xp < 1000:
        return "Beginner", 1
    elif xp < 5000:
        return "Intermediate", 2
    elif xp < 10000:
        return "Advanced", 3
    else:
        return "Expert", 4

for xp in [500, 2500, 7500, 15000]:
    level_name, level_num = check_level(xp)
    print(f"\nXP {xp}: {level_name} (Level {level_num})")


# NONE RETURN (Implicit)
def print_welcome():
    """
    Agar return statement na ho toh function None return karta hai
    """
    print("\nWelcome to CodeArena!")
    # No return statement

result = print_welcome()
print(f"Return value: {result}")  # None


# EARLY RETURN
def validate_player(age, email):
    """
    Early return - condition match hote hi return kar do
    """
    if age < 13:
        return False, "Age must be 13+"
    
    if "@" not in email:
        return False, "Invalid email format"
    
    if "." not in email.split("@")[1]:
        return False, "Email must have domain"
    
    return True, "Player validated successfully"

# Test validation
print("\n--- Validation Tests ---")
test_cases = [
    (10, "kid@email.com"),      # Fail: age
    (20, "invalid-email"),       # Fail: format
    (20, "test@domain"),         # Fail: no extension
    (20, "valid@email.com")      # Pass
]

for age, email in test_cases:
    is_valid, message = validate_player(age, email)
    status = "✓" if is_valid else "✗"
    print(f"{status} Age: {age}, Email: {email} -> {message}")
