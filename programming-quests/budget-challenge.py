'''
Problem: BUDGET TRACKER

You’re building a simple budget tracker for a personal finance app.
Write a function called track_budget(income, expenses) that:
Takes two lists of numbers:
> income: amounts earned from different sources.
> expenses: amounts spent.

Calculates total income, total expenses, and remaining balance.
Returns a string summary that looks like this:
Income: X, Expenses: Y, Balance: Z

'''
def track_budget(income, expenses, balance):
    balance += income - expenses
    print(f"Income: {income}, Expenses: {expenses}, Balance: {balance}")
    return balance

balance = 100
balance = track_budget(10,20,balance)