'''
No-Index Syntax
In my opinion, Python has the most elegant syntax for iterating directly over the items in a list without worrying about index numbers. If you don't need the index number you can use the following syntax:



tree, the variable declared using the in keyword, directly accesses the value in the list rather than the index of the value. If we don't need to update the item and only need to access its value then this is a more clean way to write the code.
'''

trees = ['oak', 'pine', 'maple']
for tree in trees:
    print(tree)
# Prints:
# oak
# pine
# maple