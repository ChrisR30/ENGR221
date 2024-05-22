"""
Author: Christian Rojo
File Name: boardDisplay.py
Date: 20 May 2024
Description: Creates and displays the graphics
    based on the current state of the board.
"""

import pygame
from preferences import Preferences

screen = pygame.display.set_mode((800, 600))

class BoardDisplay:
    def __init__(self):
        # The display where the board is drawn
        self.__display = pygame.display.set_mode((Preferences.GAME_BOARD_WIDTH, Preferences.GAME_BOARD_HEIGHT))
        # Image to show as the "head"
        self.headImage = None

    def updateGraphics(self, gameData):
        """ Re-draws the board, food, and snake based
            on the current state of the board """
        
        # Clear the board
        self.clear()

        # Draw the board
        # TODO Add your code to draw the board here!
        # You may find the below drawSquare method helpful
        for row in range(0,Preferences.NUM_CELLS_TALL): # Iterate through each row on the board
            for col in range(0,Preferences.NUM_CELLS_WIDE): # Iterate through each column in the row
                cell = gameData.getCell(row, col) # Get the cell at the current row and col
                self.drawSquare(cell) # Draw the cell on the board

        # Display the score
        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(gameData.score), True, (255,255,255))
        screen.blit(text, (10,10))

        # Draw the game over message, if appropriate
        if gameData.getGameOver():
            self.displayGameOver()

        # Update the display
        pygame.display.update()

    def clear(self):
        """ Resets the background of the display """
        self.__display.fill(Preferences.COLOR_BACKGROUND)

    def drawSquare(self, cell):#row, col, cellColor):
        """ Draws a cell-sized square at the given location.
            Inputs: row - row coordinate of the square to draw
                    col - column coordinate of the square to draw
                    cellColor - color of the square to draw """
        row = cell.getRow()
        col = cell.getCol()

        if cell.isHead() and self.headImage:
            self.drawImage(row, col, self.headImage)
        else:
            cellColor = cell.getCellColor()
            pygame.draw.rect(self.__display, cellColor, [col*Preferences.CELL_SIZE, row*Preferences.CELL_SIZE, 
                                                     Preferences.CELL_SIZE, Preferences.CELL_SIZE])

    def drawImage(self, row, col, image):
        """ Displays an image at the given cell location.
            Inputs: row - row coordinate to draw the image at
                    col - column coordinate to draw the image at
                    image - the pygame image to draw """

        # First, convert the image to a Surface type (with transparent background)
        image = image.convert_alpha()
        # You will want to uncomment the below line if you want your image to fit within one cell
        #image = pygame.transform.scale(image, (Preferences.CELL_SIZE, Preferences.CELL_SIZE))
        # Grab the dimensions of the image
        imageRect = image.get_rect()
        # Place the image in the center of the given cell coordinates
        imageRect.center = ((col*Preferences.CELL_SIZE) + (Preferences.CELL_SIZE / 2),
                            (row*Preferences.CELL_SIZE) + (Preferences.CELL_SIZE / 2))
        # Place the image on the display
        self.__display.blit(image, imageRect)

    def displayGameOver(self):
        """ Displays the game over message """

        # Get the font
        font = Preferences.GAME_OVER_FONT
        # Create the text
        text = font.render(Preferences.GAME_OVER_TEXT, True, Preferences.GAME_OVER_COLOR)
        # Get the dimensions of the text box
        textRect = text.get_rect()
        # Specify the location of the text
        textRect.center = (Preferences.GAME_OVER_X, Preferences.GAME_OVER_Y)
        # Place the game over text on the display
        self.__display.blit(text, textRect)