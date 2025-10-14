'''
RPG Character Status Checker – Written Problem

You are designing a game system that needs to describe the condition of a character. Each character has:
1. A health level
2. A mana level
3. A status effect (can be “poisoned”, “stunned”, or “none”)

Your task is to determine what message to show for the character based on the following rules:

1. If the character has no health, they are dead. Ignore any other conditions.
2. If the character has very low health, they are critically injured.
3. If the character has low mana, but their health is okay, they are exhausted.
4. If the character is poisoned and alive, show poisoned but alive.
5. If the character is stunned and alive, show stunned but alive.
6. If none of the above applies, show healthy and ready.

Your job:
1. Think about the order in which you would check the conditions.
2. Decide which messages should take priority if multiple conditions might apply.
3. Write down, in words or pseudocode, how you would check and report the character’s status.
'''

def character_condition(health, mana, status):
    if health == 0:
        return "dead"
    elif health < 5 and health > 0:
        return "critically injured"
    elif status == 'stunned' and health > 0:
        return "stunned but alive"
    elif status == 'poisoned' and health > 0:
        return "poisoned but alive"
    elif mana < 5 and health > 0:
        return "exhausted"
    else:
        return "healthy and ready"
    
print(character_condition(1, 5, 'stunned'))