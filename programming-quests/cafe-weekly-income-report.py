'''
Café Weekly Income Report

Your task is to write a program that:

Asks the user to input the total income for each day (Day 1 → Day 7).
Stores these values in a list.
Uses a for loop to:
Display each day’s income with its day number.
Calculate the total and average income for the week.
'''

print("--- Weekly Income Report ---")
total = 0

for day in range(1,8):
    income = int(input(f"Day {day}: "))
    total += income

average = total / day

print("=======================")
print(f"Total Income: ₱{total}")
print(f"Average Daily Income: ₱{average}")