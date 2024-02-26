"""
Author: Christian Rojo
Filename: lab2_part1.py
Description: Improvement of the limitations of unsorted array
"""

class Array():
    #constructor
    def __init__(self, initialSizeOrValues=None ):
        if initialSizeOrValues is None: #condition 1
            self.__a = [] #begin with an empty list
        elif isinstance(initialSizeOrValues, int): #if condition 1 is false
            self.__a = [None] * initialSizeOrValues
        elif isinstance(initialSizeOrValues, list): #if condition 1 and 2 is false
            self.__a = initialSizeOrValues[:]
        else: #if all conditions are false raise exception error message
            raise ValueError("Initial value must be an integer or a list of values")
        
        self.__length = len(self.__a) #length is the length of __a

    def length(self):
        return self.__length #return the current length of the array
    def values(self):
        return self.__a #reutnr a list of the current array values
    #return the value at index idx
    #otherwise, do not return anything
    def get(self, idx):
        if 0 <= idx < self.__length: #check if idx is in bounds
            return self.__a[idx]
        
    #set the value at index idx
    def set(self, idx, value):
        if 0 <= idx < self.__length: #check if idx is in bounds
            self.__a[idx] = value

    #insert value to the end of the array
    def insert(self, value):
        self.__a.append(value)
        self.__length += 1

    #return the index of value in the array,
    # or -1 if value is not in the array
    def search(self, value):
        for idx in range(self.__length):
            if self.__a[idx] == value:
                return idx
        return -1
    
    #delete all orrcurance of value in the array
    #returns true if any orrurances were deleted, false otherwise
    def delete(self, value):
        count = 0
        idx = 0
        while idx < self.__length:
            if self.__a[idx] == value:
                del self.__a[idx]
                self.__length -= 1
                count += 1
            else:
                idx += 1
        return count > 0
    
    #print all items in the list
    def traverse(self):
        for item in self.__a:
            print(item)

if __name__ == '__main__':
    pass