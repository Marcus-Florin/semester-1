"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

import sys
from time import sleep

states = { "red":4, "red_amber":3, "green":5, "amber":3 }
states_durations = list(states.values())
states_colours = list(states)

systime = 0

try:
    maxtime = int(input())  # read an integer number of steps (>0)
    if maxtime < 1:
        raise exception()
except:
    sys.exit("Error: Must provide a non-zero, positive integer.")


# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14

while maxtime != 0:
    for colour in range(len(states_colours)):
        for duration in range(states_durations[colour]):
            if maxtime != -1:
                print(f"Time {systime:03} State {states_colours[colour]}")
                maxtime -= 1
                systime += 1
            else:
                sys.exit()

