"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""

# input validation for correct data types and non-negative/zero numerics
valid = False
while not valid:
    try:
        destination = str(input("Where are you going to? "))
        distance_miles_input = float(input("How many miles will you travel? "))
        time_hours_input = float(input("How many hours will the journey take? "))
        if distance_miles_input > 0 and time_hours_input > 0:
            valid = True
        else:
            raise Exception()
    except:
        print("Invalid Input\n")

#calculation
average_speed = distance_miles_input / time_hours_input

#output
print(f"You will travel to {destination} at an average speed of {average_speed:.2f} mph.")

# TODO: convert distance_miles_input and time_hours_input to numbers
# TODO: calculate the average speed in miles per hour
# TODO: print a summary message using an f-string
# Extension: add validation for zero or negative values
