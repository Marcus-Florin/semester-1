# Worksheet 1.2: Task 1 Solution

import sys

try:
    grade = int(input("Enter an integer grade in the range 0 to 100: "))
    if grade < 0 or grade > 100:
        raise exception()
except:
    sys.exit("Grade must be an integer between 0 and 100")

if grade < 40:
    result = "Fail"
elif grade > 69:
    result = "Distinction"
else:
    result = "Pass"

print(f"{grade} is a {result}")