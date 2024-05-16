import pytest
import random

from ..sortingFunctions import *

@pytest.fixture 
def array_to_sort(num_items=20):
    random.seed(10)
    return random.sample(range(100), num_items)

# Tests that the array is sorted using insertion sort
@pytest.mark.insertion_sort
def test_insertion_sort(array_to_sort):
    # Sort the array with insertionSort
    my_sorted_array = insertionSort(array_to_sort)
    # Create a copy of the original array to sort
    sorted_array = array_to_sort[:]
    # Sort the copy
    sorted_array.sort()
    # Check that insertionSort's output is sorted
    assert my_sorted_array == sorted_array

# Tests that the array is sorted using bubble sort
@pytest.mark.bubble_sort
def test_bubble_sort(array_to_sort):
    # Sort the array with bubbleSort
    my_sorted_array = bubbleSort(array_to_sort)
    # Create a copy of the original array to sort
    sorted_array = array_to_sort[:]
    # Sort the copy
    sorted_array.sort()
    # Check that bubbleSort's output is sorted
    assert my_sorted_array == sorted_array