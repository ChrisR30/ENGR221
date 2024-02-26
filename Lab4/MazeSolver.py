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
        self.ss = searchStructure()  # Initialize a searchStructure object

    def tileIsVisitable(self, row:int, col:int) -> bool:
        if row < 0 or col < 0 or row >= self.maze.num_rows or col >= self.maze.num_cols:
            return False #Check if tile is in bounds of maze
        tile = self.maze.contents[row][col] #get the tile at the row and column
        return tile and not tile.isWall() and not tile.visited() #check to see if tile exists, is not a wall and not visted

    def solve(self):
        # Start at the beginning of the maze
        start_tile = self.maze.start
        # Add the start tile to the search structure
        self.ss.add(start_tile)

        # Loop until the search structure is empty
        while not self.ss.isEmpty():
            # Get the next tile from the search structure
            current_tile = self.ss.remove()
            # Mark the current tile as visited
            current_tile.visit()

            # Check if the current tile is the goal
            if current_tile == self.maze.goal:
                return current_tile  # Solution found

            # Explore adjacent tiles (north, south, east, west)
            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_row, next_col = current_tile.getRow() + dr, current_tile.getCol() + dc
                if self.tileIsVisitable(next_row, next_col):
                    next_tile = self.maze.contents[next_row][next_col]
                    next_tile.setPrevious(current_tile)
                    self.ss.add(next_tile)

        return None  # No solution found

    def getPath(self):
        # Get the goal tile
        current_tile = self.solve()
        if current_tile:
            # Start from the goal tile and backtrack to the start
            path = []
            while current_tile:
                path.append(current_tile)
                current_tile = current_tile.getPrevious()
            # Reverse the path to start from the start tile
            return path[::-1]
        else:
            return []  # No solution, return an empty list

    # Print the maze with the path of the found solution
    # from Start to Goal. If there is no solution, just
    # print the original maze.
    def printSolution(self):
        # Get the solution for the maze from the maze itself
        solution = self.getPath()
        # A list of strings representing the maze
        output_string = self.maze.makeMazeBase()
        # For all of the tiles that are part of the path, 
        # mark it with a *
        for tile in solution:
            output_string[tile.getRow()][tile.getCol()] = '*'
        # Mark the start and goal tiles
        output_string[self.maze.start.getRow()][self.maze.start.getCol()] = 'S'
        output_string[self.maze.goal.getRow()][self.maze.goal.getCol()] = 'G'

        # Print the output string
        for row in output_string:
            print("".join(row))


if __name__ == "__main__":
    # The maze to solve
    maze = Maze(["____",
                 "S##E",
                 "__#_",
                 "____"])
    # Initialize the MazeSolver to be solved with a Stack
    solver = MazeSolver(maze, Stack)
    # Solve the maze and print the solution
    solver.printSolution()