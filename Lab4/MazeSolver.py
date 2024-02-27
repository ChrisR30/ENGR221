"""
Author: Christian Rojo
Filename: MazeSolver.py
Description: Algorithm to find a path in a 2D grid using stacks and queues
"""
from SearchStructures import Stack, Queue
from Maze import Maze

class MazeSolver:
    # Constructor
    # Inputs:
    #   maze: The maze to solve (Maze)
    #   searchStructure: The search structure class to use (Stack or Queue)
    def __init__(self, maze, searchStructure):
        self.maze = maze             # The maze to solve
        self.ss = searchStructure()  # Initialize a SearchStructure object

    def tileIsVisitable(self, r:int, c:int) -> bool: # Function to check if tile is visitable
        # Check if out of bounds
        if r < 0 or r >= self.maze.num_rows:    # Check if row is in bounds
            return False
        if c < 0 or c >= self.maze.num_cols:    # Check if col is in bounds
            return False
        if self.maze.contents[r][c].visited():  # Check if tile was visited
            return False
        if self.maze.contents[r][c].isWall():   # Check if tile is a wall
            return False
   
        return True

    def solve(self): # Function to solve the maze
        # add starting point to search structure
        self.ss.add(self.maze.start)
        
        while not self.ss.isEmpty(): # Continue until search structure is empty

            current = self.ss.remove() # Retrieve the next tile to check and also remove it
            self.maze.contents[current.getRow()][current.getCol()].visit() # Mark the new tile as visited

            if current == self.maze.goal: # Check if current tile is the goal
                return  # Once goal is found, terminate the function
            
            else:   # Check neighboring tiles and add them to the search structure if vistable

                if (self.tileIsVisitable(current.getRow() - 1, current.getCol())): # North
                    self.maze.contents[current.getRow() - 1][current.getCol()].setPrevious(current) # Set previous to current
                    self.ss.add(self.maze.contents[current.getRow() - 1][current.getCol()]) # Insert into stack if visitable

                if (self.tileIsVisitable(current.getRow() + 1, current.getCol())): # South
                    self.maze.contents[current.getRow() + 1][current.getCol()].setPrevious(current) # Set previous to current
                    self.ss.add(self.maze.contents[current.getRow() + 1][current.getCol()]) # Insert into stack if visitable

                if (self.tileIsVisitable(current.getRow(), current.getCol() + 1)): # East
                    self.maze.contents[current.getRow()][current.getCol() + 1].setPrevious(current) # Set previous to current
                    self.ss.add(self.maze.contents[current.getRow()][current.getCol() + 1]) # Insert into stack if visitable

                if (self.tileIsVisitable(current.getRow(), current.getCol() - 1)): # West
                    self.maze.contents[current.getRow()][current.getCol() - 1].setPrevious(current) # Set previous to current
                    self.ss.add(self.maze.contents[current.getRow()][current.getCol() - 1]) # Insert into stack if visitable
        return # End

    def getPath(self): # Function to for path from goal to start
        current = self.maze.goal

        if current.getPrevious() == None: 
            return [] # If no previous tile, return list empty
            
        path = []
        
        while (current != None): # Traverse through previous tiles until reaching start
            path.append(current)
            current = current.getPrevious()

        return path     
    
    # Print the maze with the path of the found solution
    # from Start to Goal. If there is no solution, just
    # print the original maze.
    def printSolution(self): # Function to print maze with found path from start to goal

        solution = self.getPath() # Get the solution for the maze from the maze itself
        output_string = self.maze.makeMazeBase() # A list of strings representing the maze

        for tile in solution:
            output_string[tile.getRow()][tile.getCol()] = '*' # Mark all tiles in solution
        
        output_string[self.maze.start.getRow()][self.maze.start.getCol()] = 'S' # Mark the start tile
        output_string[self.maze.goal.getRow()][self.maze.goal.getCol()] = 'G'  # Mark the goal tile

        for row in output_string:
            print(row) # Print the output string

   

if __name__ == "__main__": # Main block for testing
    # The maze to solve
    maze = Maze(["____",
                 "S##G",
                 "__#_",
                 "____"])
    solver = MazeSolver(maze, Stack) # Initialize the MazeSolver to be solved with a Stack
    solver.solve() # Solve the maze
    solver.printSolution() # Print the solution