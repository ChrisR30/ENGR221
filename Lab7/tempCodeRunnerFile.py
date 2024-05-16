    # print(box.findAllNicknames())  # Output should be a list of all nicknames

    # # Test adding an entry
    # added = box.add("nickname1", "species1")
    # print(added)  # Output should be True if added successfully
    # print(box.findEntryByNickname("nickname1"))  # Output should be the Entry object

    # # Test adding a duplicate entry
    # added = box.add("nickname1", "species1")
    # print(added)  # Output should be False since it's a duplicate

    # # Test finding an entry
    # found_entry = box.find("nickname1", "species1")
    # print(found_entry)  # Output should be the Entry object

    # # Test removing an entry by nickname
    # removed = box.removeByNickname("nickname1")
    # print(removed)  # Output should be True if removed successfully
    # print(box.findEntryByNickname("nickname1"))  # Output should be None since its removed

    # # Test removing an entry by nickname and species
    # box.add("nickname2", "species2")
    # removed = box.removeEntry("nickname2", "species2")
    # print(removed)  # Output should be True if removed successfully
    # print(box.findEntryByNickname("nickname2"))  # Output should be None since its removed