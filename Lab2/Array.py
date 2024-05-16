"""
Author: Prof. Alyssa and Christian Rojo
Filename: array.py
Description: Implementation of an unsorted array with duplicates
"""

class Array():
    # Constructor
    def __init__(self, initialSizeOrElements):
        if type(initialSizeOrElements) == int: # Make sure the input is an integer
            self.__a = [None] * initialSizeOrElements # Initialize array with 'None' values multiplied by initial size
            self.__length = initialSizeOrElements  # Store the initial size as the length of the array
            self.__maxLength = initialSizeOrElements # Store the initial size as the max length
        else: 
            self.__a = initialSizeOrElements # Set the array equal to list that is passed in
            self.__length = len(initialSizeOrElements) # Get the length of the list passed in
            self.__maxLength = self.__length # Set maxLength eqaul to length of list

    ########
    # Methods
    ########
        
    # Return the current length of the array
    def length(self):
        return self.__length 
    
    # Return a list of the current array values
    def values(self):
        return self.__a

    # Return the value at index idx
    def get(self, idx):
      if 0 <= idx and idx < self.__length: # Check if idx is in bounds
         return self.__a[idx]              # Return the item at index idx
 
    # Set the value at index idx
    def set(self, idx, value):         
      if 0 <= idx and idx < self.__length: # Check if idx is in bounds
         self.__a[idx] = value             # Set the item at index inx to value
    
    # Insert value to the end of the array
    def insert(self, value):
        if self.__maxLength <= self.__length: # Check if there is enough space in array
            self.__a += [None] * 2 # Increase size of array by two 
            self.__maxLength = len(self.__a) # Update max length

        self.__a[self.__length] = value # Insert the value at the current size of length
        self.__length += 1 # Increment the length by 1
           
    # Return the index of value in the array or an empty list if its not there
    def search(self, value):
        indexes = [] # Initialize an empty list to collect all indexes of duplicates
        for idx in range(self.__length): # Loop through the array
            if self.__a[idx] == value:  # Check if the value at the current index matches value
                indexes.append(idx) # If values match then add index to array   
        return indexes  # Return the list of indexes                  

    # Delete the first occurrence of value in the array
    # Returns True if value was deleted, False otherwise
    def delete(self, value):
        idx = self.search(value) # Get list of indexes that are duplicates
        for i in range(len(idx)): # Loop through the list of indexes 
            if i != 0: # Decrement the index by one after the first index because array will be shifted
                idx[i] = idx[i] - 1
            self.__length -= 1 # Decrement the array length

            # Shift all the remaining values 
            for j in range(idx[i], self.__length):
                self.__a[j] = self.__a[j+1]
            if i == len(idx) - 1: # if the array is done looping then recreate the array to remove the excess values
                self.__a = self.__a[0:self.__length]
   
    # Print all items in the list
    def traverse(self):
        for i in range(self.__length): # Loop through the array
            print(self.__a[i]) # Print each item

if __name__ == '__main__':
    pass
