"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.

try:
    amount_per_month = int(input(f"Okay {name}, how much do you want to save each month? "))
except:
    print("Invalid Input")
    exit()


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.

amount_per_year = amount_per_month * 12
print(f"You will save £{amount_per_year} per year.")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

interest = amount_per_year * 0.008
amount_with_interest = amount_per_year + interest
print(f"With interest, you with save £{amount_with_interest:.2f} per year.")
