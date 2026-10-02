"""Advanced Task 5: Safe Divider
- Ask for a numerator and a denominator.
- Convert both inputs to integers and divide them to get a result.
- Use try/except to catch both non-numeric input and division by zero, giving useful messages for each case.
- Only print the final answer when the calculation succeeds.
"""

valid = False
while not valid:
    try:
        numerator_input = int(input("Enter the numerator: "))
        denominator_input = int(input("Enter the denominator: "))
        if numerator_input == 0 or denominator_input == 0:
            print("Please enter non-zero inputs.")
        else:
            valid = True
    except:
        print("Please enter inputs that are numbers with no decimals.")

answer = numerator_input / denominator_input

print(answer)

# TODO: wrap the risky operations in a try/except block
# TODO: convert the values to integers and perform the division
# TODO: print clear feedback when something goes wrong
# TODO: only show the answer when the division succeeds
