"""
Name: Christian Rojo
File name: randomWalker.py
Description: Implementation of a random walker's steps using a loop rather than recursion
Date: 03/29/2024
"""

import random  
import time

def rs():
    """rs chooses a random step and returns it.
       Note that a call to rs() requires parentheses.
       Arguments: none at all!
    """
    return random.choice([-1, 1])

def rwpos(start, nsteps):
    """ rwpos models a random walker that
        * starts at the int argument, start
        * takes the int # of steps, nsteps

        rwpos returns the final position of the walker.
    """
    time.sleep(0.1)
    print('location is', start)
    if nsteps == 0:
        return start
    else:
        newpos = start + rs()  # take one step
        return rwpos(newpos, nsteps - 1)

def rwsteps(start, low, hi):
    """ rwsteps models a random walker which
        * is currently at start 
        * is in a walkway from low (usually 0) to hi (max location) 
          
        rwsteps returns the # of steps taken 
        when the walker reaches an edge
    """
    walkway = "_"*(hi-low)    # create a walkway of underscores
    S = (start-low)           # this is our sleepwalker's location, start-low

    walkway = walkway[:S] + "S" + walkway[S:]  # put our sleepwalker, "S", there

    walkway = " " + walkway + " "              # surround with spaces, for now...

    print(walkway, "    ", start, low, hi)     # print everything to keep track...
    time.sleep(0.05)

    if start <= low or start >= hi:            # base case: no steps if we're at an endpt
        return 0
    
    else:
        newstart = start + rs()                # takes one step, from start to newstart
        return 1 + rwsteps(newstart, low, hi)  # counts one step, recurses for the rest!

def rwstepsLoop(start, low, hi):
    walkway = "_" * (hi - low)                 # Representation of the walkway with underscores
    S = start - low                            # The position of the walker on the walkway
    walkway = walkway[:S] + "S" + walkway[S:]  # Putting the walker's position in the walkway
    walkway = " " + walkway + " "              # Spaces to the begnning and end of the walkway for format
    print(walkway, "    ", start, low, hi)     # Print the walkway with the current position and bounds
    

    steps = 0                                  # Initialize steps to 0
    while low < start < hi:                    # Loop to simulate the walker's movement
        start += rs()                          # Random step
        steps += 1                             # Increment step by 1
        S = start - low                        # The position of the walker on the walkway
        walkway = "_" * (hi - low)             # Update the position of the walker on the walkway
        walkway = walkway[:S] + "S" + walkway[S:]
        walkway = " " + walkway + " "          # Formatting with spaces in beginning and end
        print(walkway, "    ", start, low, hi) # Print the updated walkway with the current position
        

    return steps                               # Return the total number of steps

if __name__ == '__main__':
    print(rs())