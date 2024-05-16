"""
Author: Christian Rojo
node.py
Represents a Node in a singly linked list
Date: 03/28/2024
"""

class Node():

    def __init__(self, value, next=None):
        self.__value = value    # The value of the node
        self.__nextNode = next  # The next node in the list

    ###########
    # Methods #
    ###########

    # Return whether the given node is the first in the list
    def isFirst(self) -> bool:
        return self.__nextNode == None

    #####
    # Getters
    #####
        
    # Return the value of the node
    def getValue(self):
        return self.__value 
    
    # Return the next node in the list
    def getNextNode(self):
        return self.__nextNode
    
    #####
    # Setters
    #####

    # Set the value of the node to a new value
    def setValue(self, new_value) -> None:
        self.__value = new_value 

    # Set the next node to a new node
    def setNextNode(self, new_next) -> None:
        # Confirm that the input is a valid node
        if self.__checkValidNode(new_next):
            self.__nextNode = new_next 

    #####
    # Helpers
    #####

    # Check whether the input node is a valid Node or None
    # Return True if it is, or raise an exception if not
    def __checkValidNode(self, node) -> bool:
        if type(node) != Node and node != None:
            raise Exception("Error: Input must be a valid Node or None")
        return True
    
    # This overloads the built in __str__ method and will
    # be run when printing a node (e.g., print(node))
    def __str__(self) -> str:
        return str(self.getValue())
    
if __name__ == "__main__":
    pass