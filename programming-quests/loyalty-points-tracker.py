'''
"The Loyalty Points Tracker"

Scenario:

You’ve been asked to automate the loyalty points system for a café (of course ☕).
Here’s how it works:

Every ₱100 spent gives the customer 10 points.

If the customer spends ₱500 or more in a single visit, they earn a bonus of 50 points.

The café wants to know how many total points the customer earned after several visits.
'''
print("=== Loyalty Points Tracker ===")

customerVisit = int(input("Enter Number of Visits: "))

total_spent = 0
total_points = 0

for i in range(1, customerVisit + 1):
    customerCost = int(input(f"How much did you spend on visit #{i}?: "))
    total_spent += customerCost

    # base points: 10 points for every ₱100
    points = (customerCost // 100) * 10 # so no remainders 

    # bonus: if ₱500 or more, +50 points
    if customerCost >= 500:
        points += 50

    print(f"Visit #{i}: Earned {points} points")
    total_points += points

average_spent = total_spent / customerVisit

print("\n=== Summary ===")
print(f"Total visits: {customerVisit}")
print(f"Total amount spent: ₱{total_spent}")
print(f"Total loyalty points earned: {total_points}")
print(f"Average spend per visit: ₱{average_spent:.2f}")
