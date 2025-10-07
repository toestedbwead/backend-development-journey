'''
The Challenge: POTION CRAFTER

You’re designing a simple potion system for a game.
Each potion has a base potency and a bonus multiplier that depends on the player’s level.

Requirements:
1. Define a global variable for player_level.
2. Write a function called brew_potion(base_potency, ingredient_bonus) that returns the potion’s final strength.
The potion’s strength should depend on all three values:
> the base_potency,
> the ingredient_bonus, and
> the global player_level.

Then, write a print statement that outputs: The potion's final strength is X.
'''

player_level = 20

def brew_potion(base_potency, ingredient_bonus):
    final_strength = (base_potency + ingredient_bonus) * player_level
    return final_strength
    
final = brew_potion(70,10)
print(f"The potion's final strength is {final}")