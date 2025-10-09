'''
Floor Division

You’re splitting treasure among adventurers.

Task: Write a function split_treasure(total_gold, adventurers) that returns how much gold each adventurer gets without fractions.
'''

def split_treasure(total_gold, adventurers):
    total_gold = total_gold // adventurers
    return total_gold

print(split_treasure(5,3))

'''
Exponents

Magic spell power scales with level.

Task: Write a function magic_spell(base_power, level) that returns the total power by raising base_power to the power of level.
'''

def magic_spell(base_power, level):
    total_power = base_power ** level
    return total_power

print(magic_spell(5,2))

'''
Scientific Notation

The wizard academy can train enormous numbers of students.

Task: Write a function academy_capacity() that returns 3 numbers using scientific notation:

Small academy: 2,500,000

Medium academy: 25,000,000

Large academy: 250,000,000
'''

def academy_capacity():
    small_acad = 2.5e6
    medium_acad = 2.5e7
    large_acad = 2.5e8
    return small_acad, medium_acad, large_acad

print(academy_capacity())