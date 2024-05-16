"""
Author: Christian Rojo
linkedList.py
Implementation of a singly linked list
Date: 03/28/2024
"""

from node import Node 

class LinkedList():
    
    def __init__(self):
        self.__firstNode = None # The first node in the list

    ###########
    # Methods #
    ###########
        
    # Return whether or not the list is empty
    def isEmpty(self) -> bool:
        return self.getFirstNode() == None

    # Return the value of the first node in the list
    def first(self):
        # Raise an exception if the list is empty
        if self.isEmpty():
            raise Exception("Error: List is empty, cannot return first  value")
        return self.getFirstNode().getValue()

    # Return the first node in the list
    def getFirstNode(self) -> Node:
        return self.__firstNode
    
    # Set the first node of the list to a new node
    def setFirstNode(self, node) -> None:
        # Raise an exception if the input is not a valid node
        if node != None and type(node) != Node:
            raise Exception("Error: Input must be valid Node or None")
        else:
            self.__firstNode = node 
    
    # Return the node containing the given value in the list.
    # If the value is not in the list, return None.
    def find(self, value) -> Node:
        # Traverse down the list, starting with the first node
        node = self.getFirstNode()
        while node != None:
            # If this node has the given value, return it
            if node.getValue() == value:
                return node 
            # Otherwise, grab the next node to check
            node = node.getNextNode()
        # If the value was not found, return None
        return None

    # Insert the given value to the front of the list
    def insert(self, value) -> None:
        # Create a new node that points to the first node in the list
        node = Node(value, self.getFirstNode())
        # Set the new node to be the first in the list
        self.setFirstNode(node)

    # Insert the given value_to_add into the list after after_value.
    # Return True if inserted successfully, or False if after_value
    # is not found in the list.
    def insertAfter(self, value_to_add, after_value) -> bool:
        # Find the node with value after_value
        node = self.find(after_value)
        # If the value was not found, return False
        if node == None:
            return False 
        # Otherwise, create a new node with value_to_add that
        # points to the node after the one with after_value
        newNode = Node(value_to_add, node.getNextNode())
        # Set after_value's next node to be the new node
        node.setNextNode(newNode)
        # Return True that the item was inserted successfully
        return True
    
    # Delete the first node from the list and return the value
    # of the node that was deleted
    def deleteFirstNode(self) -> None:
        # If we try to delete from an empty list, raise an exception
        if self.isEmpty():
            raise Exception("Error: List is empty")
        # Otherwise, grab the first node of the list
        first = self.getFirstNode()
        # Set the first node of the list to the second node
        self.setFirstNode(first.getNextNode())
        # Return the value of the deleted node
        return first.getValue()
    
    # Delete an item with the given value from the list and return
    # True if the value was deleted, or None if it failed.
    def deleteValue(self, value) -> bool:
        # If we try to delete from an empty list, raise an exception
        if self.isEmpty():
            raise Exception("Error: Cannot delete from empty list")
        # Otherwise, traverse down the list starting with the first node
        previous = self.getFirstNode()
        while previous.getNextNode() != None:
            # Get the next node in the list
            next = previous.getNextNode() 
            # Check whether we want to delete the next node
            if value == next.getValue():
                # If so, change the next node of the previous node
                # to be the next node of the one we are deleting
                previous.setNextNode(next.getNextNode())
                # Return that the value was deleted
                return True
            # Update previous to be the next item in the list
            previous = next 
        # If the value was not found, raise an exception
        raise Exception("Error: Cannot find value {} in list".format(value))

    # Print each item in the list from beginning to end
    def traverse(self) -> None:
        # Traverse starting from the first node
        node = self.getFirstNode()
        # Stop when we reach the end of the list
        while node != None:
            # Print the value of this node
            print(node.getValue())
            # Update node to be the next node
            node = node.getNextNode()

    # This overloads the built in __len__ method and will be run
    # when checking the length of a linkedList (e.g., len(linkedList))
    def __len__(self) -> int:
        # A counter starting at 0
        l = 0
        # Traverse down the list starting with the first node
        node = self.getFirstNode() 
        # Stop when we reach the end of the list
        while node != None:
            # Increment the counter for each node we find
            l += 1
            # Update node to be the next node
            node = node.getNextNode()
        # Return the counter
        return l 
    
    # This overloads the built in __str__ method and will be 
    # run when printing a linked list (e.g., print(linkedList)).
    # Outputs the list in format "[val1 > val2 > ... > valn]"
    def __str__(self) -> str:
        # Begin the string with the left bracket
        out = "["
        # Traverse down the list starting with the first node
        node = self.getFirstNode() 
        # Stop when we reach the end of the list
        while node != None:
            # Only add the arrow if there's more than one value in the list
            if len(out) > 1:
                out += " > "
            # Add the value of the current node to the string
            out += str(node)
            # Update node to be the next node
            node = node.getNextNode()
        # Add the closing bracket and return the string
        return out + "]"
    
if __name__ == "__main__":
    pass