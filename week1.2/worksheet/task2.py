# Worksheet 1.2: Task 2 Solution

from util import read_numbers
import sys


numbers = read_numbers()

try:
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
except:
    sys.exit("Error: no numbers provided")

numbers = sorted(numbers)


print(len(numbers)/2)
if len(numbers) % 2 == 0:
    median = (numbers[int(len(numbers)/2)] + numbers[int((len(numbers)/2)-1)]) / 2
else:
    median = numbers[int((len(numbers)/2) - 0.5)]

print(f"""
Minimum = {minimum}
Maximum = {maximum}
Mean = {average}
Median = {median}
"""
)