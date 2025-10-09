'''
Mini-App: RPG Character Manager

Scenario:
You are creating a tiny console app to manage your RPG character’s stats, inventory, and energy. The app should let you:

View stats
Spend energy
Rest to regain energy
Track inventory items (add and remove items)
Track coins (income and spending)

Requirements:
Variables
player_level → integer
player_current_energy → integer
player_coins → integer
inventory → a list of strings

Functions
view_stats() → prints level, energy, and coins
spend_energy(amount) → decreases energy by amount safely (can’t go below 0)
rest(minutes) → increases energy by minutes
add_item(item) → adds an item to inventory
remove_item(item) → removes an item if it exists
earn_coins(amount) → adds coins
spend_coins(amount) → subtracts coins safely (can’t go negative)

Constraints & Tips:
Use parameters and return values instead of global whenever possible
Use print statements to debug intermediate values
Handle “invalid” cases gracefully (e.g., spending more energy than available)
Keep your code modular — each function should do one clear thing
'''



# decreases energy by amount safely (can’t go below 0)
def spend_energy(energy, amount):
    energy = energy - amount
    if energy <= 0 :
        print("You are out of energy!")
        return 0
    else :
        return energy
    
energy = spend_energy(100, 30)


# increases energy by minutes
def rest(energy, minutes):
    energy = energy + minutes
    return energy

energy = rest(energy, 10)

inventory = ["sword", "shield", "helmet"]

# adds an item to inventory
def add_item(item, inventory):
    pass

# removes an item if it exists
def remove_item(item):
    pass


# adds coins
def earn_coins(coins, amount):
    coins += amount
    return coins

coins = earn_coins(100,20)

# subtracts coins safely (can’t go negative)
def spend_coins(coins, amount):
    coins -= amount
    if coins < 0 :
        print("Not enough coins!")
        return 0
    else:
        return coins
    
coins = spend_coins(coins,50)



#  prints level, energy, and coins
def view_stats(level, energy, coins):
    return(f"Level: {level}, Energy: {energy}, Coins: {coins}")

stats = view_stats(30,energy,coins)
print(stats)