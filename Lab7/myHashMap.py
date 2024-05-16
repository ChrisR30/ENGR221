"""
Name: Christian Rojo
File name: myHashMap.py
Description: Implementation of a hash map
Date: 03/30/2024
"""

class MyHashMap:
    def __init__(self, load_factor=0.75, initial_capacity=16):
        self.load_factor = load_factor
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

        """
    Resizes the self.buckets array when the load_factor is reached. """
    def resize(self):
        # Double the number of buckets
        self.capacity *= 2 
        # Create a new set of buckets that's twice as big as the old one
        new_buckets = [[] for _ in range(self.capacity)]
        # Add each key, value pair already in the MyHashMap to the new buckets
        for bucket in self.buckets:
            if bucket != []:
                for entry in bucket:
                    index = hash(entry.getKey()) % self.capacity
                    new_buckets[index].append(entry)
                    #self.put(entry.getKey(), entry.getValue())
        # Update the self.buckets attribute with the new entries
        self.buckets = new_buckets

    """
    Adds the specified key, value pair to the MyHashMap if 
    the key is not already in the MyHashMap. If adding a new key would
    surpass the load_factor, resize the MyHashMap before adding the key.
    Return true if successfully added to the MyHashMap.
    Raise an exception if the key is None. """
    def put(self, key, value):
        if key is None: # Check if key is none and raise exception if it is
            raise ValueError("Key cannot be None")
        hash_value = hash(key) # Compute the hask value of key
        index = hash_value % self.capacity # Calculate index in the hash table
        bucket = self.buckets[index] # Select bucket based on index
        for entry in bucket: # Iterate through entries in the bucket
            if entry.getKey() == key: # If key exists update the value and return it
                entry.setValue(value)
                return
        new_entry = self.MyHashMapEntry(key, value) # Create a new entry if key doesnt exist
        bucket.append(new_entry) # Add entry to the bucket
        self.size += 1 #Increment size by 1
        if self.size > self.capacity * self.load_factor: # Check if resizing is needed
            self.resize() # Resize has table if load factor exceeded

    """
    Replaces the value that maps to the given key if it is present.
    Input: key is the key whose mapped value is being replaced.
           newValue is the value to replace the existing value with.
    Return true if the key was in this MyHashMap and replaced successfully.
    Raise an exception if the key is None. """
    def replace(self, key, newValue):
        if key is None: # Check if key is none and raise exception if it is
            raise ValueError("Key cannot be None")
        hash_value = hash(key) # Compute the hash value of key
        index = hash_value % self.capacity # Calculate index in the hash table
        bucket = self.buckets[index] # Select bucket based on index
        for entry in bucket: # Iterate through entries in the bucket
            if entry.getKey() == key: # If key exists replace value and return true
                entry.setValue(newValue)
                return True
        return False # If no key found return false

    """
    Remove the entry corresponding to the given key.
    Return true if an entry for the given key was removed.
    Raise an exception if the key is None. """
    def remove(self, key):
        if key is None: # Check if key is none and raise exception if it is
            raise ValueError("Key cannot be None")
        hash_value = hash(key)  # Compute hash value of key
        index = hash_value % self.capacity  # Calculate index in the hash table
        bucket = self.buckets[index]    # Select bucket based on index
        for i, entry in enumerate(bucket):  # Iterate through entries in the bucket
            if entry.getKey() == key:   # If key is found remove it and return true
                del bucket[i]
                self.size -= 1
                return True
        return False # Return false if not found

    """
    Adds the key, value pair to the MyHashMap if it is not present.
    Otherwise, replace the existing value for that key with the given value.
    Raise an exception if the key is None. """
    def set(self, key, value):
        if key is None: # Check if key is none and raise exception if it is
            raise ValueError("Key cannot be None")
        self.put(key, value) # Call put method to add/update entry

    """
    Return the value of the specified key. If the key is not in the
    MyHashMap, return None.
    Raise an exception if the key is None. """
    def get(self, key):
        if key is None: # Check if key is none and raise exception if so
            raise ValueError("Key cannot be None")
        hash_value = hash(key) # Compute hash value
        index = hash_value % self.capacity # Calculate index in the hash table
        bucket = self.buckets[index] # Select bucket based on index
        for entry in bucket: # Iterate through entries in the bucket
            if entry.getKey() == key: # If key is found return value
               return entry.getValue()
        return None # Return none if key not found

    """
    Return the number of key, value pairs in this MyHashMap. """
    def size(self):
        return self.size # Returns the number of key value pairs

    """
    Return true if the MyHashMap contains no elements, and 
    false otherwise. """
    def isEmpty(self): # Checks if myhashmap is empty
        return self.size == 0

    """
    Return true if the specified key is in this MyHashMap. 
    Raise an exception if the key is None. """
    def containsKey(self, key):
        if key is None: 
            raise ValueError("Key cannot be None")
        hash_value = hash(key)
        index = hash_value % self.capacity
        bucket = self.buckets[index]
        for entry in bucket:
            if entry.getKey() == key: # If key is found return true
                return True
        return False # If key not found return false

    """
    Return a list containing the keys of this MyHashMap. 
    If it is empty, return an empty list. """
    def keys(self):
        all_keys = []
        for bucket in self.buckets:
            for entry in bucket:
                all_keys.append(entry.getKey()) # Append key to the list
        return all_keys # Return the list of keys

    class MyHashMapEntry:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def getKey(self):
            return self.key

        def getValue(self):
            return self.value

        def setValue(self, new_value):
            self.value = new_value

if __name__ == '__main__':
    # Test basic functionality

    hashmap = MyHashMap()

    entry1 = MyHashMap.MyHashMapEntry("chris", "30")
    hashmap.put(entry1.getKey(), entry1.getValue())
    entry2 = MyHashMap.MyHashMapEntry("ian", "11")
    hashmap.put(entry2.getKey(), entry2.getValue())
    entry3 = MyHashMap.MyHashMapEntry("jordan", "23")
    hashmap.put(entry3.getKey(), entry3.getValue())

    hashmap.set("poole","3")

    print(hashmap.buckets)
    print(hashmap.keys())
    print(hashmap.size)
    print(hashmap.get("ian"))

    hashmap.replace("ian", "12")

    print(hashmap.get("ian"))
    print(hashmap.containsKey("jordan"))
    print(hashmap.containsKey("klay"))

    hashmap.remove("chris")
    print(hashmap.keys())
    """
    hashmap = MyHashMap()
    hashmap.put("key1", "value1")
    hashmap.put("key2", "value2")
    print(hashmap.buckets)
    print(hashmap.get("key2"))
    hashmap.replace("key1", "value3")
    print(hashmap.get("key1"))
    print(hashmap.containsKey("key3"))
    print(hashmap.keys())
    """