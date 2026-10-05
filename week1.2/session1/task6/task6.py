# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)

music = {
    "Queen": 
    [
    [1973, "Queen"],
    [1974, "Queen II"],
    [1974, "Sheer Heart Attack"],
    [1975, "A Night at the Opera"],
    [1976, "A Day at the Races"],
    [1977, "News of the World"],
    [1978, "Jazz"],
    [1980, "The Game"],
    [1980, "Flash Gordon"],
    [1982, "Hot Space"],
    [1984, "The Works"],
    [1986, "A Kind of Magic"],
    [1989, "The Miracle"],
    [1991, "Innuendo"],
    [1995, "Made in Heaven"]
],
    "Fleetwood Mac": 
    [
    [1968, "Fleetwood Mac"],
    [1968, "Mr. Wonderful"],
    [1969, "Then Play On"],
    [1970, "Kiln House"],
    [1971, "Future Games"],
    [1972, "Bare Trees"],
    [1973, "Penguin"],
    [1973, "Mystery to Me"],
    [1974, "Heroes Are Hard to Find"],
    [1975, "Fleetwood Mac"],
    [1979, "Tusk"],
    [1982, "Mirage"],
    [1987, "Tango in the Night"],
    [1990, "Behind the Mask"],
    [1995, "Time"],
    [2003, "Say You Will"]
],
    "The Beatles": 
    [
    [1963, "Please Please Me"],
    [1963, "With the Beatles"],
    [1964, "A Hard Day's Night"],
    [1964, "Beatles for Sale"],
    [1965, "Help!"],
    [1965, "Rubber Soul"],
    [1966, "Revolver"],
    [1967, "Sgt. Pepper's Lonely Hearts Club Band"],
    [1968, "The Beatles"],
    [1969, "Abbey Road"],
    [1970, "Let It Be"]
],
    "The Turtles": 
    [
    [1965, "It Ain't Me Babe"],
    [1966, "You Baby"],
    [1967, "Happy Together"],
    [1968, "The Turtles Present the Battle of the Bands"],
    [1969, "Turtle Soup"]
],
}

# Pretty-print the data structure

pprint(music, width=100, sort_dicts=True)

# Display details of one album recorded by a specific artist

queen = music.get("Queen")
print(queen[3])

# Counting total number of albums

album_list = list(music.items())

total = 0
for band in range(0,len(album_list)):
    total += len(album_list[band][1])

print(total)