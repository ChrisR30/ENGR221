"""
Name: Christian Rojo
File name: hashmap_tests.py
Description: Tests for myHashMap.py
Date:
03/30/2024
"""
import pytest

from myHashMap import MyHashMap

"""
This first test checks if a value added to the hashmap
using the put method can be retrieved correctly using
the get method
"""

def test_put_and_get():
    hashmap = MyHashMap()
    hashmap.put("key1", "value1")
    assert hashmap.get("key1") == "value1"

"""
This tests checks that the replace method properly
replaces the value associated with a key in the hashmap
"""

def test_replace():
    hashmap = MyHashMap()
    hashmap.put("key1", "value1")
    hashmap.replace("key1", "new_value1")
    assert hashmap.get("key1") == "new_value1"

"""
This tests verifies that the remove method correctly
removes an entry from the hashmap
"""

def test_remove():
    hashmap = MyHashMap()
    hashmap.put("key1", "value1")
    hashmap.remove("key1")
    assert hashmap.get("key1") is None