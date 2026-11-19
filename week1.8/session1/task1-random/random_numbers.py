import random

# Get user to input how many random numbers they want

try:
    number_count = int(input("Number of random numbers: "))
except:
    raise TypeError("Input must be an integer.")

if number_count <= 0:
    raise ValueError("Input must be greater than zero.")

# Generate this many random numbers

random_numbers = []

for a in range(number_count):
    random_numbers.append(random.randint(1,100))

# Write the random numbers to a file named random.txt, one number per line

with open("random.txt","w") as infile:

    for number in random_numbers:
        infile.write(f"{str(number)}\n")
