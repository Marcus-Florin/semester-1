"""Advanced Task 2: Budget Breakdown
- Ask for three separate expense amounts (for example: travel, food, accommodation).
- Convert each input so you can add them together to get a total trip cost.
- Calculate the average spend per category and show each value with an f-string.
- Extension: format the totals so they always show two decimal places.
"""

#inputs and validation
valid = False
while not valid:
    try:
        travel_cost_input = float(input("Travel cost in pounds: "))
        food_cost_input = float(input("Food cost in pounds: "))
        accommodation_cost_input = float(input("Accommodation cost in pounds: "))
        if travel_cost_input >= 0 and food_cost_input >= 0 and accommodation_cost_input >= 0:
            valid = True
        else:
            raise exception()
    except:
        print("Invalid Input\n")
    
#calculate total and average
total_cost = travel_cost_input + food_cost_input + accommodation_cost_input
average_cost = total_cost / 3

#output
print(f"""
Your trip breakdown:

Travel       - £{travel_cost_input:.2f}
Food         - £{food_cost_input:.2f}
Accomodation - £{accommodation_cost_input:.2f}

Avg per Cat  - £{average_cost:.2f}
Total        - £{total_cost:.2f}
""")
# TODO: convert each value to a number type that supports decimals
# TODO: calculate the total and the average spend per category
# TODO: print the three costs, the total, and the average
# Extension: format the totals to two decimal places
