"""
================================================================================
CodeArena Day 1 - Example 2: Basic Arithmetic Operations
================================================================================
"""

# Example 2: XP Calculation System
# Is example mein hum arithmetic operations sikhte hain

# Player ke current XP
base_xp = 1000                    # Current XP points

# Match win karne par XP add hota hai
win_bonus = 250                   # Win karne par bonus XP

# Level up hone par XP multiply hota hai
level_multiplier = 1.5            # Level multiplier

# 1. ADDITION (+) - XP add karna
# Do values ko add karne ke liye + operator use karte hain
total_xp = base_xp + win_bonus    # 1000 + 250 = 1250
print(f"Base XP: {base_xp}")
print(f"Win Bonus: {win_bonus}")
print(f"Total XP (Addition): {total_xp}")

# 2. SUBTRACTION (-) - XP penalty
# Penalty points minus karne ke liye
penalty = 50                      # Penalty for leaving match
remaining_xp = total_xp - penalty  # 1250 - 50 = 1200
print(f"\nPenalty applied: {penalty}")
print(f"Remaining XP: {remaining_xp}")

# 3. MULTIPLICATION (*) - Level bonus
# Level ke hisaab se XP multiply hota hai
level_bonus_xp = remaining_xp * level_multiplier  # 1200 * 1.5 = 1800
print(f"\nLevel Multiplier: {level_multiplier}x")
print(f"XP after multiplier: {level_bonus_xp}")

# 4. DIVISION (/) - Average XP calculation
matches_played = 5                # Total matches khele
avg_xp_per_match = remaining_xp / matches_played  # 1200 / 5 = 240.0
print(f"\nMatches played: {matches_played}")
print(f"Average XP per match: {avg_xp_per_match}")

# 5. FLOOR DIVISION (//) - Integer division
# Decimal hata kar sirf integer value
int_avg = remaining_xp // matches_played  # 1200 // 5 = 240
print(f"Integer Average: {int_avg}")

# 6. MODULO (%) - Remainder
# Division ke baad bacha hua
remainder = remaining_xp % matches_played  # 1200 % 5 = 0
print(f"Remainder: {remainder}")

# 7. EXPONENTIATION (**) - Power calculation
# XP growth rate calculate karne ke liye
growth_rate = 2 ** 3              # 2 ki power 3 = 8
print(f"\nXP Growth Rate: {growth_rate}")

# Complex calculation - Sab operations ek saath
final_xp = (base_xp + win_bonus - penalty) * level_multiplier
print(f"\n=== FINAL CALCULATION ===")
print(f"Formula: (base + bonus - penalty) * multiplier")
print(f"({base_xp} + {win_bonus} - {penalty}) * {level_multiplier}")
print(f"Final XP: {final_xp}")

# Output sab calculations ka summary
print("\n=== Summary ===")
print(f"Addition: {base_xp} + {win_bonus} = {base_xp + win_bonus}")
print(f"Subtraction: {base_xp + win_bonus} - {penalty} = {base_xp + win_bonus - penalty}")
print(f"Multiplication: {base_xp + win_bonus - penalty} * {level_multiplier} = {(base_xp + win_bonus - penalty) * level_multiplier}")
