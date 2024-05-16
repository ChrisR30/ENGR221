"""
Name: Christian Rojo
Filename: myset.py
Date: 02/06/2023

"""

class MySet:

    #Constructor
    def __init__(self, values):
        self.set = []                            # Initialize an empty list to store values in the set
        self.length = 0                          # Initialize length of set to 0
        self.max_length = 0                      # Initialize maximum length of set to 0
        for i in range(len(values)):             # Iterate through each value in the input values
            self.insert(values[i])               # Insert values into the set using the insert method
    
    #Return size of set
    def size(self):
        return self.length                       # Return the current length of the set
    
    #Return values in set
    def vals(self):
        return self.set                          # Return the list containing all values in the set

    #Loop array and check if there is match           
    def search(self, value):
        for i in range(self.length):             # Loop through the set
            if value == self.set[i]:             # Check if the value matches any value in the set
                return True                      # Return true if matched
        return False                             # Return false if no match
    
    #Insert function
    def insert(self, value):
        if self.search(value) == False:          # Check if the value is not already in the set
            if self.length >= self.max_length:   # Check if the length of set exceeds max length
                self.set += [None] * 1           # Expand the set for accommodation of one more value
                self.max_length = len(self.set)  # Update max length of the set
            self.set[self.length] = value        # Insert the value into the set at the current length
            self.length += 1                     # Increment the length of the set by 1

    def traverse(self):
       if self.isEmpty():                        # Check if set is empty
            print("Set is Empty!")               # Print an alert indicating an empty set
       else: 
            for i in range(self.length):         # Loop the the set
                print(self.set[i])               # Print the values in the set

    def delete(self, value):
        if self.isEmpty():                       # Check if set is empty
            print("Nothing to delete, set is empty!") # Print an alert indicating an empty set
        else: 
            for i in range(self.length):         # Loop though set
                if value == self.set[i]:         # Check if the given value matches any value in the set
                    self.swap(i)                 # If matched swap the values and update the length
                    return
                
    # Swap the values at final and matched index, since order does not matter
    def swap(self, i):
        self.set[i] = self.set[self.length - 1]  # Swap the value at i with the last value in the set
        self.set = self.set[0:self.length]       # Remove the last value of the set
        self.length -= 1                         # Decrement length of the set
        
    #Check if set is empty
    def isEmpty(self):
        if self.length > 0:                      # Check if length of the set is greater than 0
            return False                         # Return false if the set in not empty
        return True                              # Return true if the set is empty
    
if __name__ == '__main__':
    pass