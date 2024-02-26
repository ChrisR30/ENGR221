#import pytest

from ..SearchStructures import Stack, Queue 
from ..Maze import Maze
from ..MazeSolver import MazeSolver

def test_maze_small_horizontal(capfd):
    maze = Maze(["S___G"])
    solver = MazeSolver(maze, Stack)
    solver.solve()
    solver.printSolution()
    out, _ = capfd.readouterr()
    assert out == "['S', '*', '*', '*', 'G']\n"

def test_maze_small_vertical(capfd):
    maze = Maze(["S",
                 "_",
                 "_",
                 "_",
                 "G"])
    solver = MazeSolver(maze, Queue)
    solver.solve()
    solver.printSolution()
    out, _ = capfd.readouterr()
    assert out == "['S']\n['*']\n['*']\n['*']\n['G']\n"

def test_maze_med_stack(capfd):
    maze = Maze(["____",
                 "S##G",
                 "__#_",
                 "____"])
    solver = MazeSolver(maze, Stack)
    solver.solve()
    solver.printSolution()
    out, _ = capfd.readouterr()
    assert out == "['_', '_', '_', '_']\n" + \
                  "['S', '#', '#', 'G']\n" + \
                  "['*', '*', '#', '*']\n" + \
                  "['_', '*', '*', '*']\n"
    
def test_maze_med_queue(capfd):
    maze = Maze(["____",
                 "S##G",
                 "__#_",
                 "____"])
    solver = MazeSolver(maze, Queue)
    solver.solve()
    solver.printSolution()
    out, _ = capfd.readouterr()
    assert out == "['*', '*', '*', '*']\n" + \
                  "['S', '#', '#', 'G']\n" + \
                  "['_', '_', '#', '_']\n" + \
                  "['_', '_', '_', '_']\n"
    
def test_maze_no_solution(capfd):
    maze = Maze(["_#__",
                 "S##G",
                 "__#_",
                 "__#_"])
    solver = MazeSolver(maze, Queue)
    solver.solve()
    solver.printSolution()
    out, _ = capfd.readouterr()
    assert out == "['_', '#', '_', '_']\n" + \
                  "['S', '#', '#', 'G']\n" + \
                  "['_', '_', '#', '_']\n" + \
                  "['_', '_', '#', '_']\n"

def test_maze_big_stack(capfd):
    maze = Maze(["##____#_##",
                 "#____##__#",
                 "_S#_______",
                 "__##_____#",
                 "____####__",
                 "#____##___",
                 "#__##___#_",
                 "___##___##",
                 "#___#__G__",
                 "_______###",])
    solver = MazeSolver(maze, Stack)
    solver.solve()
    solver.printSolution()
    out, _ = capfd.readouterr()
    assert out == \
            "['#', '#', '_', '_', '_', '_', '#', '_', '#', '#']\n" + \
            "['#', '_', '_', '_', '_', '#', '#', '_', '_', '#']\n" + \
            "['*', 'S', '#', '_', '_', '_', '_', '_', '_', '_']\n" + \
            "['*', '*', '#', '#', '_', '_', '_', '_', '_', '#']\n" + \
            "['_', '*', '*', '*', '#', '#', '#', '#', '_', '_']\n" + \
            "['#', '*', '*', '*', '_', '#', '#', '_', '_', '_']\n" + \
            "['#', '*', '*', '#', '#', '_', '_', '_', '#', '_']\n" + \
            "['_', '*', '*', '#', '#', '*', '*', '*', '#', '#']\n" + \
            "['#', '*', '*', '*', '#', '*', '*', 'G', '_', '_']\n" + \
            "['_', '_', '_', '*', '*', '*', '*', '#', '#', '#']\n"
    
def test_maze_big_queue(capfd):
    maze = Maze(["##____#_##",
                 "#____##__#",
                 "_S#_______",
                 "__##_____#",
                 "____####__",
                 "#____##___",
                 "#__##___#_",
                 "___##___##",
                 "#___#__G__",
                 "_______###",])
    solver = MazeSolver(maze, Queue)
    solver.solve()
    solver.printSolution()
    out, _ = capfd.readouterr()
    assert out == \
            "['#', '#', '_', '_', '_', '_', '#', '_', '#', '#']\n" + \
            "['#', '_', '_', '_', '_', '#', '#', '_', '_', '#']\n" + \
            "['_', 'S', '#', '_', '_', '_', '_', '_', '_', '_']\n" + \
            "['_', '*', '#', '#', '_', '_', '_', '_', '_', '#']\n" + \
            "['_', '*', '*', '_', '#', '#', '#', '#', '_', '_']\n" + \
            "['#', '_', '*', '_', '_', '#', '#', '_', '_', '_']\n" + \
            "['#', '_', '*', '#', '#', '_', '_', '_', '#', '_']\n" + \
            "['_', '_', '*', '#', '#', '_', '_', '_', '#', '#']\n" + \
            "['#', '_', '*', '*', '#', '_', '*', 'G', '_', '_']\n" + \
            "['_', '_', '_', '*', '*', '*', '*', '#', '#', '#']\n"