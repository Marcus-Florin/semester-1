import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

try:
    name_count = int(input("Number of names: "))
except:
    raise TypeError("Input must be an integer.")

if name_count <= 0:
    raise ValueError("Input must be greater than zero.")

if name_count > 100:
    raise ValueError("Input must be less than or equal to 100")

random_selections = []

for a in range(name_count):

    while True:
        random_selection = random.randint(1,100)

        if not random_selection in random_selections:
            break

    random_selections.append(random_selection)

    print(names[random_selection])