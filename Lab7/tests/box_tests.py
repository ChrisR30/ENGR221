import pytest

from box import Box

"""
This test checks the functionality of
adding an entry to the box and finding it
"""
def test_add_and_find():
    box = Box()
    box.add("nickname1", "species1")
    entry = box.findEntryByNickname("nickname1")
    assert entry is not None
    assert entry._Entry__nickname == "nickname1"  # Accessing private attribute directly
    assert entry._Entry__species == "species1"   # Accessing private attribute directly

"""
This tests checks how the box
handles adding duplicate entries
"""
def test_duplicate_add():
    box = Box()
    box.add("nickname1", "species1")
    added = box.add("nickname1", "species1")
    assert not added

"""
This test checks the funcionality of
removing an entry from the box by nickname
"""
def test_remove_by_nickname():
    box = Box()
    box.add("nickname1", "species1")
    removed = box.removeByNickname("nickname1")
    assert removed
    assert box.findEntryByNickname("nickname1") is None

