"""
Maze.py
Class for the maze to traverse
Adapted from UCSD CSE 12
"""

from Tile import Tile

# Maze to traverse
class Maze():
    # Constructor
    # maze_spec: a list of strings specifying the maze
    def __init__(self, maze_spec):
        self.num_rows = None    # Number of rows in the maze (int)
        self.num_cols = None    # Number of columns in the maze (int)
        self.contents = None    # The contents of the maze (Tile[][])
        self.start = None       # The starting location (Tile)
        self.goal = None         # The goal location (Tile)
        self.initializeMaze(maze_spec)  # Iniitalizes the maze using the given specification

    # Initializes the Maze from the maze_spec
    def initializeMaze(self, maze_spec):
        # Set the number of rows in the maze
        self.num_rows = len(maze_spec)
        # Set the number of columns in the maze
        self.num_cols = len(maze_spec[0])
        # Initialize a list of lists with the dimensions of the maze
        self.contents = [[None for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        # Iterate through each character in maze_spec and assign the appropriate Tile value
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                # Get the character in the maze_spec
                char = maze_spec[i][j]
                # A blank tile
                if char == '_':
                    self.contents[i][j] = Tile(i, j, False)
                # A wall
                elif char == '#':
                    self.contents[i][j] = Tile(i, j, True)
                # Start tile
                elif char == 'S':
                    self.contents[i][j] = Tile(i, j, False)
                    self.start = self.contents[i][j]
                # Goal tile
                elif char == 'G':
                    self.contents[i][j] = Tile(i, j, False)
                    self.goal = self.contents[i][j]

    # Generate the base maze as a list of lists of characters
    # (Only contains blank tiles and walls, not start or goal)
    def makeMazeBase(self):  
        # Create a list of lists of blank tiles
        maze_list = [["_" for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        # Iterate through all the maze contents
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                # Get the tile at the current cell
                tile = self.contents[row][col]
                # If the tile is a wall, change the maze_list character
                if tile.isWall():
                    maze_list[row][col] = "#"
        # Return the completed base maze
        return maze_list
        
if __name__ == "__main__":
    pass