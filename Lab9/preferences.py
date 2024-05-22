"""
Author: Christian Rojo
File Name: prefrences.py
Date: 20 May 2024
Description: Stores values for constant variables.
"""

import pygame

class Preferences:
    pygame.init()

    ##########
    # Timing #
    ##########

    # How frequently to move the snake
    REFRESH_RATE = 2
    # How frequently to add food to the board
    FOOD_ADD_RATE = 25    
    # How long to sleep between updates
    SLEEP_TIME = 30

    ##########
    # Sizing #
    ##########

    # Dimensions of the board
    NUM_CELLS_WIDE = 50
    NUM_CELLS_TALL = 30 

    # Size of each cell in pixels
    CELL_SIZE = 30

    # Dimensions of the board in pixels
    GAME_BOARD_WIDTH = NUM_CELLS_WIDE * CELL_SIZE
    GAME_BOARD_HEIGHT = NUM_CELLS_TALL * CELL_SIZE

    ##########
    # Colors #
    ##########

    COLOR_BACKGROUND = pygame.Color('lavender')
    COLOR_WALL = pygame.Color('gray40')
    COLOR_FOOD = pygame.Color('firebrick')
    COLOR_EMPTY = pygame.Color('lavender')
    COLOR_HEAD = pygame.Color('darkorchid4')
    COLOR_BODY = pygame.Color('darkorchid1')

    ##########################
    # Game over text display #
    ##########################
    
    GAME_OVER_X = GAME_BOARD_HEIGHT / 2
    GAME_OVER_Y = GAME_BOARD_WIDTH / 2
    GAME_OVER_COLOR = pygame.Color('navy')
    GAME_OVER_FONT = pygame.font.SysFont("arial", 120)
    GAME_OVER_TEXT = "Game Over"

    ######################
    # Graphics and Audio #
    ######################

    # Image to display as the head
    HEAD_IMAGE = "trainer.png"
    # Sound to play when eating
    EAT_SOUND = "meow.wav"