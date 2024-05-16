"""
Name: Christian Rojo
File name: deque.py
Description: Implementation of a deque class
Date: 03/28/2024
"""

from .doublyLinkedList import DoublyLinkedList

class Deque():
    def __init__(self):                       # Initializes an empty deque
        self.__values = DoublyLinkedList()    # Deque is initialized with an instance of doublyinkedlist

    def isEmpty(self):                        # Checks if deque is empty by checking the linked list
        return self.__values.isEmpty()        # Returns bool - true if empty false otherwise
    
    def __len__(self):                        # Returns the number of elements
        return len(self.__values)             # Returns int - number of elements in the deque
    
    def __str__(self):                        # Returns a string of the deque
        return str(self.__values)             # Returns str - string representation of the deque

    def peekLeft(self):                       # Returns the value of the leftmost element of the deque without removing it
        return self.__values.first()          # Returns the value of the leftmost element

    def peekRight(self):                      # Returns the value of the rightmost element of the deque without removing it
        return self.__values.getLastNode().getValue() # Returns the value of the rightmost element

    def insertLeft(self, value):              # Inserts a new element at the left end of the deque
        self.__values.insertFront(value)      # Arguments - the value to be inserted into the deque
        
    def insertRight(self, value):             # Inserts a new element at the right end of the deque
        self.__values.insertBack(value)       # Arguments - the value to be inserted into the deque

    def removeLeft(self):                     # Removes and returns the leftmost element
        return self.__values.deleteFirstNode() # Returns - value of the removed element

    def removeRight(self):                    # Removes and returns the rightmost element
        return self.__values.deleteLastNode() # Returns - value of the removed element
    
if __name__ == "__main__":
    pass