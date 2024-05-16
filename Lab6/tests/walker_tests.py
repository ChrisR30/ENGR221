import pytest

import randomWalker as rw

def test_rwstepsLoop_low():
    steps = rw.rwstepsLoop(-10, 0, 10)
    # Check the "base case" low
    assert steps == 0

def test_rwstepsLoop_hi():
    steps = rw.rwstepsLoop(20, 0, 10)
    # Check the "base case" high
    assert steps == 0

def test_rwstepsLoop(capfd):
    # Run the loop
    rw.rwstepsLoop(5, 0, 10)
    # Capture the output
    out, _ = capfd.readouterr()
    # Split the string into a list, separated by newlines
    out_lines = out.split('\n')
    # Check that the last printed line is formatted as expected
    assert out_lines[-2] in [' __________S       10 0 10', 
                             ' S__________       0 0 10']