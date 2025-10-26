'''
Assignment
Our player is selling the items in their inventory to the shopkeep!

Pop the last element from the inventory list until there is nothing left. Pop the elements into an item variable so that each prints in turn on line 19.
'''

def clear_inventory():
    inventory = [
        "Healing Potion",
        "Iron Bar",
        "Kite Shield",
        "Shortsword",
        "Leather Scraps",
        "Tattered Cloth",
    ]

    print(f"inventory: {inventory}")

    # don't touch above this line

    for i in range(0, len(inventory)):
        item = inventory.pop()

        # don't touch below this line
        print(f"Selling: {item}")
        print(f"inventory: {inventory}")

# BEST PRACTICE CODE
'''
At the start of your loop, len(inventory) is calculated once (say it’s 6), and Python will loop exactly 6 times — that’s the same number of pops needed to empty the list. So in this specific case, it behaves exactly as intended.

But — and this is why I mentioned it — in real-world code, if the inventory changed inside the loop for another reason (like a condition or another function call), that for loop wouldn’t adapt to the new length.

The while len(inventory) > 0: version dynamically checks the length each time, so it’s just a bit safer and more flexible.
'''
def test():
    clear_inventory()
    print("=====================================")


def main():
    test()


main()
