'''
Exercise 1: Floor Division

Scenario:
You’re designing a loot distribution system for a game. After a big boss fight, the total coins dropped should be shared evenly among all players. Any leftover coins that can’t be evenly divided go to the system (they’re lost).

Task:
Write a function called distribute_loot(total_coins, players) that returns how many coins each player gets.
Use the correct type of division so you only give out whole coins.
'''

def distribute_loot(total_coins, players):
    return total_coins // players

print(distribute_loot(500,17))