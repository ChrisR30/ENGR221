"""
Name: Christian Rojo
File name: doublyLinkedList.py
Description: Implementation of a doubly linked list
Date: 03/28/2024
"""

from .doubleNode import DoubleNode 

class DoublyLinkedList():

    def __init__(self):
        self.__firstNode = None # Initialize the first and last nodes as none
        self.__lastNode = None 

    def isEmpty(self):
        return self.getFirstNode() is None # Check if the list is empty by checking if the first node is none

    def first(self):
        if self.isEmpty(): # Get the value of the first node in the list
            raise Exception("Error: List is empty")
        return self.getFirstNode().getValue()
    
    def getFirstNode(self):
        return self.__firstNode # Return the first node of the list

    def getLastNode(self):
        return self.__lastNode # Return the last node of the list
    
    def setFirstNode(self, node): # Set the first node of the list
        if type(node) != DoubleNode and node != None: # Check if input is a valid DoubleNode or none
            raise Exception("Error: Input must be valid") # Exception raised if input is invalid
        self.__firstNode = node 

    def setLastNode(self, node): # Set the last node of the list
        if type(node) != DoubleNode and node != None: # Check if input is a valid DoubleNode or none
            raise Exception("Error: Input must be valid") # Exception raised if input in invalid
        self.__lastNode = node 

    def find(self, value):
        node = self.getFirstNode() # Traverse down the list, starting with the first node and a given value
        while node != None:
            if node.getValue() == value: # If this node has the given value, return it
                return node 
            node = node.getNextNode() # Otherwise, grab the next node to check
        return None # If the value was not found, return None

    def insertFront(self, value): # Insert a new node with the given value to the front of the list
       node = DoubleNode(value)
       if self.isEmpty(): # Check if the lsit is empty
            self.setFirstNode(node) # Set the first node to the new node
            self.setLastNode(node) # Set the last node to the new node
       else:
           node.setNextNode(self.getFirstNode()) # If the list is not empty adjust pointers accordingly
           self.getFirstNode().setPreviousNode(node)
           self.setFirstNode(node)    

    def insertBack(self, value): # Insert a node with the given value to the back of the list
        if self.isEmpty(): # If the list is empty
            node = DoubleNode(value, self.getFirstNode(),self.getLastNode())
            self.setFirstNode(node) # Set first node to the new node
            self.setLastNode(node) # Set last node to the new node
        else:
           node = DoubleNode(value, None, self.getLastNode()) # If the list is not empty adjust pointers accordingly
           self.getLastNode().setNextNode(node)
           self.setLastNode(node)

    def insertAfter(self, value_to_add, after_value) -> None: # Insert a new node with the given value after the node with the specified value
        node = self.find(after_value) # Find the node after which the new node will be inserted
        if node == None: # If the node is not found return false
            return False
        nextNode = node.getNextNode()
        newNode = DoubleNode(value_to_add, nextNode, node)
        node.setNextNode(newNode)
        if nextNode == None: self.setLastNode(newNode) # If the inserted node is the last node then update LastNode
        else: # If not adjust pointers accordingly
            nextNode.setPreviousNode(newNode)
        return True

    def deleteFirstNode(self): # Delete the first node from the list
        if self.isEmpty(): # Check if the list is empty
            raise Exception("Error: List is empty") # If empty raise exception for error
        firstNode = self.getFirstNode()
        if firstNode.isLast(): # If the first node is also the last node empty the list
           self.setFirstNode(None)
           self.setLastNode(None)
           return firstNode.getValue()
        firstNode.getNextNode().setPreviousNode(None) # If not adjust accordingly
        self.setFirstNode(firstNode.getNextNode())
        return firstNode.getValue()
    
    def deleteLastNode(self): # Delete the last node from the list
       if self.isEmpty(): # Check if empty
           raise Exception("Error: List is empty") # Raise exception for error
       last = self.getLastNode()
       if last.isFirst(): # If the last node is also the first node empty the list
           self.setFirstNode(None)
           self.setLastNode(None)
           return last.getValue()
       last.getPreviousNode().setNextNode(None) # If not adjust accordinly
       self.setLastNode(last.getPreviousNode())
       return last.getValue()
    
    def deleteValue(self, value): # Delete the node with the specified value from the list
        if self.isEmpty(): # Check if the list is empty
            raise Exception("Error: Cannont delete from empty list") # Raise exception for error
        previousNode = self.getFirstNode() # Previous node is first node
        while previousNode.getNextNode() != None: 
            nextNode = previousNode.getNextNode() # Next node is next node
            if value == nextNode.getValue(): # Previous and next nodes point to each other
                nextNode.getNextNode().setPreviousNode(previousNode)
                previousNode.setNextNode(nextNode.getNextNode())

                return value
            previousNode = next
        raise Exception("Error: Cannot find value {} in list".format(value)) # Raise exception for error

    def forwardTraverse(self):
        node = self.getFirstNode() # Traverse starting from the first node to the last node
        while node != None:
            print(node.getValue())  # Print the value of this node
            node = node.getNextNode() # Update node to be the next node

    def reverseTraverse(self): # Traverse starting from the last node to the first node
        node = self.getLastNode()
        while node != None:
            print(node.getValue()) # Print the value of this node
            node = node.getPreviousNode() # Update node to be the previous node

    def __len__(self): # Return the length of the list
        lc = 0 # Length counter
        node = self.getFirstNode() # Traverse down the list starting with the first node
        while node != None:
            lc += 1 # Increment the counter for each node we find
            node = node.getNextNode() # Update node to be the next node
        return lc # Return the counter
    
    def __str__(self) -> str: # Return a string representation of the list
        out = "[" # Left bracket in the beginning
        node = self.getFirstNode() # Traverse down the list starting with the first nod
        while node != None:
            if len(out) > 1: # Only add the arrow if there's more than one value in the list
                out += " <-> " # Two arrows since its a doubly
            out += str(node)# Add the value of the current node to the string
            node = node.getNextNode() # Update node to be the next node
        return out + "]" # Right bracket at the end
    
    
if __name__ == "__main__":
    pass