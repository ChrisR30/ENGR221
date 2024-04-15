"""
Name: Christian Rojo
File name: binarySearchTree.py
Description: Implementation of a binary search tree
Date: 04/09/2024
"""

class BinarySearchTree:
    """Implementation of a class
    representing a binary search tree
    with several methods. 8 to be exact.
    """

    def __init__(self):
        self.__root = None # The root Node of the BST

    def insert(self, insertKey, insertValue):
        """ Inserts the given key and value into the BST.
            Inputs:
                - insertKey: (any) The key to insert
                - insertValue: (any) The value to insert
            Returns: None
        """
        # Update the root to include the inserted node
        self.__root = self.__insertHelp(self.__root, insertKey, insertValue)
    
    def __insertHelp(self, node, insertKey, insertValue):
        """ A recursive helper method to insert a new node 
            with the given key and value into the BST.
            Inputs:
                - node: (Node) The root of the subtree to insert into
                - insertKey: (any) The key to insert
                - insertvalue: (any) The value to insert
            Returns: The node to insert """
        # Base case - Insert the node as a leaf in the appropriate location
        if node == None:
            return self.__Node(insertKey, insertValue)
        # Insert the key into the left subtree if it is less than the current key
        elif insertKey < node.key:
            node.left = self.__insertHelp(node.left, insertKey, insertValue)
        # Insert the key into the right subtree if it is greater than the current key
        elif insertKey > node.key:
            node.right = self.__insertHelp(node.right, insertKey, insertValue)
        # Return the node with the node inserted
        return node

    def isEmpty(self):
        """ Check tree to see if empty
        Arguments: None
        Output: boolean: true if empty false otherwise
        """
        return self.__root is None
    
    def getRoot(self):
        """ Get the root node of the tree 
        Arguments: None
        Output: the root node
        """
        return self.__root

    def search(self, goalKey):
        """ Search for a node with given key in tree """
        return self.__searchHelp(self.__root, goalKey)

    def __searchHelp(self, node, goalKey):
        """ A recursive method to help with the search() method, which
        searches for a given key in the BST.
        Arguments:
            node (Node): The root node of the subtree being searched.
            goalKey: The key to search for.
        output:
            Node: The Node with the key goalKey, or None if not found.
        """
        if node is None or node.key == goalKey: # Base case: if node is none or matches goalkey
            return node # Return none
        elif goalKey < node.key:
            return self.__searchHelp(node.left, goalKey) # Recursively search in the left subtree
        else:
            return self.__searchHelp(node.right, goalKey) # Recursively search in the right subtree

    def lookup(self, goal):
        """ Lookup the value associated with a given key 
        Arguments: goal - the key whose value to return
        output: the value associated with the given key
        """
        node = self.search(goal) # Search for the key
        if node is not None: # If the node is found
            return node.value # Return the value
        else:
            return None # Return none if not found

    def findSuccessor(self, subtreeRoot):
        """ Finds the successor node in the tree """
        return self.__findSuccessorHelp(subtreeRoot)
    
    def __findSuccessorHelp(self, node):
        """ Recursive function called in findSuccessor method 
        which finds the smallest key in the tree
        Arguments: The root node of the subtree to find the successor
        output: the successor node
        """
        # Base case: If the node has no left child, it is the successor
        if node.left is None:
            return node
        # Recursively search in the left subtree
        return self.__findSuccessorHelp(node.left)
    
    def delete(self, deleteKey):
        """ Deletes a node with given key """
        if self.search(deleteKey):
            self.__root = self.__deleteHelp(self.__root, deleteKey) # Added updating the root to delete method
            return self.__deleteHelp(self.__root, deleteKey)
        raise Exception("Key not in tree.")
    
    def __deleteHelp(self, node, deleteKey):
        """ Recursive method to help the delete method
        There are 3 cases which are a node with 0, 1 or 2 children
        Arguments:
            node - the root node of the subtree to delete from
            deletekey - the key to delete
        output: The updated node with specified node deleted
        """
        if node is None: # Base case
            return node
        if deleteKey < node.key: # If current node is greater than deletekey recursively delete from left subtree
            node.left = self.__deleteHelp(node.left, deleteKey)
        elif deleteKey > node.key: # If deletekey is greater than node recursively delete from right subtree
            node.right = self.__deleteHelp(node.right, deleteKey)
        else: # Do this if delete key = node
            if node.left is None and node.right is None: # Case where node has no children
                return None # Delete node
            elif node.left is None: # Case where node only has right child
                return node.right # Replaces deleted node with right child
            elif node.right is None: # Case where node only has left child
                return node.left # Replaces deleted node with left child
            else: # Node has left and right children
                successor = self.__findSuccessorHelp(node.right) # Find successor in right subtree
                node.key, node.value = successor.key, successor.value # Swap node's key and value with successor's
                node.right = self.__deleteHelp(node.right, successor.key) # Delete successor from subtree
        return node # Return updated node

    def traverse(self) -> None:
        """ Traverses tree in order """
        self.__traverseHelp(self.__root)

    def __traverseHelp(self, node) -> None:
        """ recusive method to help traverse in ascending order
        arguments: node - the root node of the subtree to traverse
        """
        if node: # If the node is not None
            self.__traverseHelp(node.left) # Recursively traverse the left subtree
            print(f"({node.key}, {node.value})") # Print key and value of node
            self.__traverseHelp(node.right) # Recursively traverse the right subtree

    def __str__(self) -> str:
        """ Represent the tree as a string. Formats as 
            {(rootkey, rootval), {leftsubtree}, {rightsubtree}} """
        return self.__strHelp("", self.__root)
    
    def __strHelp(self, return_string, node) -> str:
        """ A recursive helper method to format the tree as a string. 
            Input: 
                - return_string: (string) Accumulates the final string to output
                - node: (Node) The current node to format
            Returns: A formatted string for this node. """
        # Base case - Represent an empty branch as "None"
        if node == None:
            return "None"
        # Recursively build the string to return
        # Note, this is equivalent to
        #   return "{" + node + ", " + \
        #                self.strHelp(return_string, node.left) + ", " + \
        #                self.strHelp(return_string, node.right) + "}"
        return "{{{}, {}, {}}}".format(node, 
                                       self.__strHelp(return_string, node.left), 
                                       self.__strHelp(return_string, node.right))
            

    ##############
    # NODE CLASS #
    ##############

    class __Node:
        """ Implementation of a node in a BST. Note that it is 
            private, so it cannot be accessed outside of a BST """

        def __init__(self, key, value, left=None, right=None):
            self.key = key         # The key of the root node of this tree
            self.value = value     # The value held by the root node of this tree
            self.left = left       # Points to the root of the left subtree
            self.right = right     # Points to the root of the right subtree

        def __str__(self):
            """ Represent the node as a string.
                Formats as "{key, value}" """
            return "({}, {})".format(self.key, self.value)
        
if __name__ == "__main__":
        
    bst = BinarySearchTree() # Create a binary search tree

    bst.insert(5, "five") # Insert 7 nodes with 5 being the root
    bst.insert(3, "three")
    bst.insert(8, "eight")
    bst.insert(1, "one")
    bst.insert(4, "four")
    bst.insert(7, "seven")
    bst.insert(9, "nine")

    print("BST Structure:") # Print the tree structure
    print(bst)

    print("\nroot node:") # Print original root by getting it
    r1 = bst.getRoot()
    print(r1)


    print("\nSearching for key 10:") # Search for a node
    result = bst.search(10)
    if result:
        print("Found:", result.key, result.value)
    else:
        print("Key not found.")

    
    print("\nDeleting key 5:") # Delete a node
    bst.delete(5)

    print("\nUpdated BST Structure after deletion:") # Print the updated tree structure
    print(bst)

    print("\nIn-order traversal of the BST:") # Traverse the tree
    bst.traverse()

    print("\nnew root node:") # Root after deleting oringinal root
    r2 = bst.getRoot()
    print(r2)
