''''
“The Café Order Calculator”

Scenario:
You’re helping a small café automate their order summary system. The café sells only 3 types of items:
Coffee = ₱50
Pastry = ₱35
Sandwich = ₱60

Customers can order multiple quantities of each item. The café wants a small program that calculates:
The total cost of the order.
A 10% discount if the total exceeds ₱300.
A final printed summary of the order.
'''


print("List of Menu: ")
print(f"1. Coffee, ₱50")
print(f"2. Pastry, ₱35")
print(f"3. Sandwich, ₱60")


userChoice = int(input("What will you order?: "))


def convertChoice(userChoice):
    if userChoice == 1:
        userChoice = 50
        return userChoice
    elif userChoice == 2:
        userChoice = 35
        return userChoice
    elif userChoice == 3:
        userChoice = 60
        return userChoice
    else:
        userChoice = int(input("That is not on the menu. Pick something else: "))
        return convertChoice(userChoice)

# defines the userChoice variable again to update the new assignment
userChoice = convertChoice(userChoice)

# asks the user the quantity of their order
choiceQuantity = int(input("How many of these do you want?: "))

# calculates the total cost
totalCost = userChoice * choiceQuantity

print(f"Your cost is: {totalCost}")

# gives 10% discount if order exceeds 300
def userDiscount(totalCost):
    if totalCost > 300:
        discount = totalCost * 0.10
        totalCost -= discount
        return totalCost
    else:
        return totalCost

totalCost = userDiscount(totalCost)

print(f"Your total cost is: {totalCost}")

