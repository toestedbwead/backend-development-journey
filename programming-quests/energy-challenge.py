'''
Challenge: ENERGY SYSTEM

You’re making a simple stamina system for an RPG.
You have a global variable that stores the player’s current energy level.

You must create two functions:
spend_energy(amount) → reduces the player’s energy by amount.

rest(minutes) → increases the player’s energy based on how long they rest.

Then, simulate this sequence:
Start at 100 energy.
Spend 30 energy.
Rest for 10 minutes.

Print the final energy left.
'''

player_current_energy = 100

def spend_energy(amount):
    global player_current_energy
    player_current_energy -= amount
    return

def rest(minutes):
    global player_current_energy
    player_current_energy += minutes
    return

spend_energy(30)
print(f"The final energy is {player_current_energy}")
rest(10)
print(f"The final energy is {player_current_energy}")


