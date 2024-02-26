"""
Tile.py
Defines a Tile in the Maze
Adapted from UCSD CSE12
"""

# A single unit in a maze
class Tile:
    # Constructor
    def __init__(self, row, col, isWall):
        self.__row = row            # row of the Tile (int)
        self.__col = col            # col of the Tile (int)
        self.__isWall = isWall  # Whether the Tile is a wall (bool)
        self.__visited = False  # Whether we have visited this Tile (bool)
        self.__previous = None  # The Tile we visited prior to this one (Tile)
    
    # Return the row
    def getRow(self):
        return self.__row 
    
    # Return the col
    def getCol(self):
        return self.__col
    
    # Return whether the Tile is a wall
    def isWall(self):
        return self.__isWall 
    
    # Return whether we have visited this Tile
    def visited(self):
        return self.__visited
    
    # Return the previous Tile
    def getPrevious(self):
        return self.__previous
    
    # Mark this Tile as visited
    def visit(self):
        self.__visited = True 

    # Set the previous Tile
    def setPrevious(self, previous):
        self.__previous = previous

    # Print out the values of this Tile
    def printAttributes(self):
        print("row: {}, col: {}, isWall: {}, visited: {}, previous: {}".format(
                    self.__row, self.__col, self.__isWall, 
                    self.__visited, self.__previous))