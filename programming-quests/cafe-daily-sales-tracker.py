'''
Scenario: “Café Daily Sales Tracker”

You’re helping a small café automate its daily sales tracking.

Every time a sale happens, the cashier enters the amount (₱).
The program should keep asking for the sale amount until the cashier enters 0, which means “end of the day.”

At the end, the program shows:

The total number of sales made that day
The total income
The average sale amount
'''

print("=== CAFE DAILY SALES TRACKER ===")

total_income = 0
total_sales = 0


sale = int(input("Input sale: "))
while sale != 0:
    total_income = total_income + sale
    total_sales += 1
    average_sale = total_income / total_sales
    sale = int(input("Input sale: "))

print(f"Total Sale: {total_sales}")
print(f"Total Income: {total_income}")
print(f"Average: {average_sale}")


