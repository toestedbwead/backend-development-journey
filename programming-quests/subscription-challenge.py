'''
Problem: SIMPLE SUBSCRIPTION TRACKER

You’re managing an app that tracks a user’s subscription payments.
Write a function called update_subscription that takes in:
balance → the user’s current wallet balance
plan_cost → the monthly subscription cost
months → the number of months to pay for

The function should:
Deduct the total cost from the balance.

Print a summary message like:
Paid for 3 months. Total cost: 900. Remaining balance: 2100

Return the updated balance.
'''

def update_subscription(balance, plan_cost, months):
    total = plan_cost * months
    balance -= total
    print(f"Paid for {months} months. Total cost: {total}. Remaining balance: {balance}")
    return balance

balance = update_subscription(1000, 700, 2)
