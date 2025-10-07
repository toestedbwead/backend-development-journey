'''
    Scope refers to where a variable or function name is available to be used. For example, when we create variables in a function (such as by giving names to our parameters), that data is not available outside of that function.

'''

def get_max_health(modifier, level):
    return modifier * level


my_modifier = 5
my_level = 10

## don't touch above this line

max_health = get_max_health(my_modifier, my_level)

# don't touch below this line

print(f"max_health is: {max_health}")
