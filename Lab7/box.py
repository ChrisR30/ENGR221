from myHashMap import MyHashMap
from entry import Entry

class Box:
    def __init__(self):
        self.nicknameMap = MyHashMap()
        self.populateBox()

    """
    Adds Entries to the Box from inputFile. Assume that each
    line in inputFile corresponds to an Entry."""
    def populateBox(self, inputFile='entries.txt'):
        # Open the file as read only
        with open(inputFile, 'r') as f:
            # Add each value in the file as an Entry to the Box
            for line in f:
                # Set the first word in the line as the nickname, and
                # the second as species
                nickname, species = line.split()
                # Add the new entry to the Box
                self.add(nickname, species)

    """
    Create an Entry object with the given information and add it
    to the nicknameMap. 
    Returns true if the Entry is successfully added to the Box, and
    false if the nickname already exists in the Box. """
    def add(self, nickname, species): 
        if self.nicknameMap.containsKey(nickname): # Check if nickname exists in the box
            return False # Return false if nickname exists
        entry = Entry(nickname, species) # Create new entry object
        self.nicknameMap.put(nickname, entry) # Add entry to nicknamemap
        return True # Return true on success


    """
    Return a single Entry object with the given nickname and species.
    Should not modify the Box itself. 
    Return None if the Entry does not exist in the Box. """
    def find(self, nickname, species):
        entry = self.nicknameMap.get(nickname) # Get entry from nicknamemap
        if entry == species:  # Check if entry exists and species match
            return entry # Return entry if found
        return None # Return none otherwise
    
    """ 
    Return a list of nickanames representing all unique 
    nicknames in the Box. Should not modify the Box itself.
    Return an empty list if the Box is empty. """
    def findAllNicknames(self):
        return self.nicknameMap.keys() # Return list of keys from nicknamemap
    
    """ 
    Return an Entry with the given nickname. Should not modify
    the Box itself. 
    Return an empty list if the nickname is not in the Box. """

    def findEntryByNickname(self, nickname):
        if self.nicknameMap.size == 0:
            return None # Empty list if nickname is not in the box
        entry = self.nicknameMap.get(nickname) # Return entry according to nickname
        return entry
    
    """
    Remove the Entry with the given nickname from the Box. 
    Return true if successful, or false otherwise."""
    def removeByNickname(self, nickname):
        return self.nicknameMap.remove(nickname) # remove entry according to nickname

    """ 
    Remove the Entry with the given nickname and species. 
    Return true if successful, or false otherwise. """
    def removeEntry(self, nickname, species):
        entry = self.find(nickname, species)# Find entry by nickname and species
        if entry: # If found remove it from box
            self.nicknameMap.remove(nickname)
            return True # Return true if successful
        return False # Return false if not found

if __name__ == '__main__':
    # Test basic functionality
  
    box = Box()
    print(box.findAllNicknames())  # Output should be a list of all nicknames

    # Test adding an entry
    added = box.add("nickname1", "species1")
    print(added)  # Output should be True if added successfully
    print(box.findEntryByNickname("nickname1"))  # Output should be the Entry object

    # Test adding a duplicate entry
    added = box.add("nickname1", "species1")
    print(added)  # Output should be False since it's a duplicate

    # Test finding an entry
    pikachu = box.findEntryByNickname("Sparky")
    print(pikachu)  # Output should be the Entry object

    # Test removing an entry by nickname
    removed = box.removeByNickname("nickname1")
    print(removed)  # Output should be True if removed successfully
    print(box.findEntryByNickname("nickname1"))  # Output should be None since its removed