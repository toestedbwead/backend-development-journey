'''
Exercise 2: Exponents

Scenario:
You’re programming a magic spell damage calculator.
Each time a spell levels up, its damage is multiplied by itself (exponentially growing power).

Task:
Write a function called spell_damage(base_damage, level) that returns the final damage after it has been raised to the power of its level.

'''

def spell_damage(base_damage, level):
    final_damage = base_damage ** level
    return final_damage

print(spell_damage(100,5))