"""Advanced Task 4: Deadline Breakdown
- Ask how many minutes remain until an assignment deadline.
- Use integer division and modulo to convert this number into days, hours, and minutes.
- Present the result using a formatted string such as "2 days, 3 hours, 15 minutes remaining".
- Extension: handle negative input by printing a warning that the deadline has already passed.
"""
days = 0
hours = 0
minutes = 0 

total_minutes = int(input("Minutes remaining until the deadline: "))

if total_minutes < 0:
    print("Deadline has already passed.")

elif total_minutes == 0:
    print("Deadline is now.")

else:
    days = total_minutes // 1440
    total_minutes -= days * 1440
    hours = total_minutes // 60
    total_minutes -= hours * 60
    minutes = total_minutes

    print(f"{days} days,{hours} hours, and {minutes} minutes remaining.")

# TODO: convert the input to an integer
# TODO: calculate whole days, leftover hours, and remaining minutes
# TODO: print the breakdown using f-strings
# Extension: detect negative values and print a warning instead
