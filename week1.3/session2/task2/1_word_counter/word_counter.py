# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

file_names = ["story.txt","story2.txt","glasses.txt"]

valid = False
while not valid:
    try:
        file_name = str(input("Enter file name: "))
        if file_name not in file_names:
            raise exception()
        else:
            valid = True
    except:
        print("Invalid Input")

# open and read the file

with open(file_name, "r") as infile:
    words = infile.read()

# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings
    words = words.split()
    print(len(words))

# display the wordcount

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210