"""
Name: Christian Rojo
File name: sortingFunctions.py
Description: Implementation of sorting algorithms.
Date: 03/27/2024
"""

import time, random

# Implementation of insertionSort algorithm
def insertionSort(list_to_sort:list) -> None:
    for i in range(len(list_to_sort)): # Iterate each index of the list
        j = i # Point j to index i
        while j > 0 and list_to_sort[j - 1] > list_to_sort[j]: # Move element found at index i to the right position in the sorted subarray
            list_to_sort[j], list_to_sort[j-1]=list_to_sort[j-1], list_to_sort[j] # Swap current element with the one before it
            j -= 1 # Move to previous index
    return list_to_sort

# Implementation of bubbleSort algorithm
def bubbleSort(list_to_sort:list) -> None:
    l = len(list_to_sort) # Get the length of list
    for i in range(l): # Iterate each element in the list
        for j in range (0, l-i-1): # Iterate each pair of elements next to
            if list_to_sort[j] > list_to_sort[j+1]: # Swap if current is greater than next
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
    return list_to_sort

# Returns a random list of the given length
def createRandomList(length:int) -> list:
    return random.sample(range(max(100, length)), length)
    
# Returns the length of time (in seconds) that it took
# for the function_to_run to sort a list of length list_length
def getRuntime(function_to_run, list_length) -> float:
    # Create a new list to sort
    list_to_sort = createRandomList(list_length)
    # Get the time before running
    start_time = time.time()
    # Sort the given list
    function_to_run(list_to_sort)
    # Get the time after running
    end_time = time.time()
    # Return the difference
    return end_time - start_time


if __name__ == '__main__':
    
    print("Insertion Sort:")
    print("Runtime for sorting 100 items:", getRuntime(insertionSort,100))
    print("Runtime for sorting 1000 items:", getRuntime(insertionSort,1000))
    print("Runtime for sorting 10000 items:", getRuntime(insertionSort,10000))
    print("Bubble Sort:")
    print("Runtime for sorting 100 items:",getRuntime(bubbleSort,100))
    print("Runtime for sorting 1000 items:",getRuntime(bubbleSort,1000))
    print("Runtime for sorting 10000 items:",getRuntime(bubbleSort,10000))
    
    A = [8,1,4,2]
    print("A = [8,1,4,2]")
    print("Running the list A through the Bubble Sort Algorithm:")
    print(bubbleSort(A))