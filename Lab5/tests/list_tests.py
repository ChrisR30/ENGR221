import pytest

from ..doublyLinkedList import DoublyLinkedList
from ..doubleNode import DoubleNode

@pytest.fixture 
# Define an empty DoublyLinkedList for testing
def emptyList():
    return DoublyLinkedList()

@pytest.fixture 
# Define a DoublyLinkedList for testing
# Should look like [3 <-> 2 <-> 1]
def nonemptyList():
    dll = DoublyLinkedList()
    dll.insertFront(1)
    dll.insertFront(2)
    dll.insertFront(3)
    return dll

####
# isEmpty
####

@pytest.mark.isEmpty
# isEmpty functionality for a DoublyLinkedList
def test_dll_isempty_true(emptyList):
    # Should return True
    assert emptyList.isEmpty()

@pytest.mark.isEmpty
# isEmpty functionality for a DoublyLinkedList
def test_dll_isempty_false(nonemptyList):
    # Should return False 
    assert not nonemptyList.isEmpty()

####
# first
####

@pytest.mark.first
# first functionality for a DoublyLinkedList
def test_dll_first(nonemptyList):
    # Check that first returns the value of the first (leftmost) item
    assert nonemptyList.first() == 3

####
# setFirstNode
####

@pytest.mark.setFirstNode
# setFirstNode functionality for a DoublyLinkedList
def test_dll_setfirstnode(nonemptyList):
    # Create a new node
    dn = DoubleNode(4)
    # Set the new node as the first node of the list
    nonemptyList.setFirstNode(dn)
    # Check that getFirstNode returns the newly set first node
    assert nonemptyList.getFirstNode() == dn

@pytest.mark.setFirstNode
# setFirstNode functionality for a DoublyLinkedList
def test_dll_setfirstnode_invalid(nonemptyList):
    # Try to set the first node of the list to an integer
    try:
        nonemptyList.setFirstNode(4)
        # The above line should have thrown an exception,
        # so this assert should not run
        assert False
    except:
        # Successfully threw an exception
        assert True

####
# setLastNode
####

@pytest.mark.setLastNode
# setLastNode functionality for a DoublyLinkedList
def test_dll_setlastnode(nonemptyList):
    # Create a new node
    dn = DoubleNode(4)
    # Set the new node as the last node of the list
    nonemptyList.setLastNode(dn)
    # Check that getLastNode returns the newly set last node
    assert nonemptyList.getLastNode() == dn

@pytest.mark.setLastNode
# setLastNode functionality for a DoublyLinkedList
def test_dll_setlastnode_invalid(nonemptyList):
    # Try to set the last node of the list to an integer
    try:
        nonemptyList.setLastNode(4)
        # The above line should have thrown an exception,
        # so this assert should not run
        assert False
    except:
        # Successfully threw an exception
        assert True

####
# find
####

@pytest.mark.find 
# find functionality for a DoublyLinkedList
def test_dll_find(nonemptyList):
    # 1 is the last (rightmost) element of nonemptyList
    assert nonemptyList.find(1) == nonemptyList.getLastNode()

@pytest.mark.find 
# find functionality for a DoublyLinkedList
def test_dll_find_notpresent(emptyList):
    # 1 is not in the empty list
    assert emptyList.find(1) == None

####
# insertFront
####

@pytest.mark.insertFront
# insertFront functionality for an empty DoublyLinkedList 
def test_dll_insertfront_empty_first(emptyList):
    # Insert a new value to the list
    emptyList.insertFront(5)
    # Check that the inserted value was set as the list's
    # first node
    assert emptyList.getFirstNode().getValue() == 5

@pytest.mark.insertFront
# insertFront functionality for an empty DoublyLinkedList 
def test_dll_insertfront_empty_last(emptyList):
    # Insert a new value to the list
    emptyList.insertFront(5)
    # Check that the inserted value was set as the list's
    # last node
    assert emptyList.getLastNode().getValue() == 5

@pytest.mark.insertFront
# insertFront functionality for a DoublyLinkedList 
def test_dll_insertfront_nonempty_first(nonemptyList):
    # Insert a new value to the list
    nonemptyList.insertFront(5)
    # Check that the inserted value was set as the list's
    # first node
    assert nonemptyList.getFirstNode().getValue() == 5

@pytest.mark.insertFront
# insertFront functionality for a DoublyLinkedList 
def test_dll_insertfront_nonempty_last(emptyList):
    # Insert a new value to the list
    emptyList.insertFront(2)
    # Insert a new value to the list
    emptyList.insertFront(1)
    # Check that the inserted value was set as the next
    # node's previous node
    assert emptyList.getLastNode().getPreviousNode().getValue() == 1

####
# insertBack
####

@pytest.mark.insertBack
# insertBack functionality for an empty DoublyLinkedList 
def test_dll_insertback_empty_last(emptyList):
    # Insert a new value to the list
    emptyList.insertBack(5)
    # Check that the inserted value was set as the list's
    # last node
    assert emptyList.getLastNode().getValue() == 5

@pytest.mark.insertBack
# insertBack functionality for an empty DoublyLinkedList 
def test_dll_insertback_empty_first(emptyList):
    # Insert a new value to the list
    emptyList.insertBack(5)
    # Check that the inserted value was set as the list's
    # first node
    assert emptyList.getFirstNode().getValue() == 5

@pytest.mark.insertBack
# insertBack functionality for a DoublyLinkedList 
def test_dll_insertback_nonempty_last(nonemptyList):
    # Insert a new value to the list
    nonemptyList.insertBack(5)
    # Check that the inserted value was set as the list's
    # last node
    assert nonemptyList.getLastNode().getValue() == 5

@pytest.mark.insertBack
# insertBack functionality for a DoublyLinkedList 
def test_dll_insertback_nonempty_first(emptyList):
    # Insert a new value to the list
    emptyList.insertBack(2)
    # Insert a new value to the list
    emptyList.insertBack(1)
    # Check that the inserted value was set as the previous
    # node's next node
    assert emptyList.getFirstNode().getNextNode().getValue() == 1

@pytest.mark.insertBack
# insertBack functionality for a DoublyLinkedList
def test_dll_insertback_nonempty_previous(nonemptyList):
    # Insert a new value to the list
    nonemptyList.insertBack(5)
    # Check that the inserted node's previous node was set
    # to the correct node
    assert nonemptyList.getLastNode().getPreviousNode().getValue() == 1

####
# insertAfter
####

@pytest.mark.insertAfter
# insertAfter functionality for a DoublyLinkedList
def test_dll_insertafter_last(nonemptyList):
    # Insert a new value to the end of the list
    nonemptyList.insertAfter(4, 1)
    # Check that the inserted value was set as the last
    # node in the list
    assert nonemptyList.getLastNode().getValue() == 4

@pytest.mark.insertAfter
# insertAfter functionality for a DoublyLinkedList
def test_dll_insertafter_notlast_prevnext(nonemptyList):
    # Insert a new value as the second element of the list
    nonemptyList.insertAfter(4, 3)
    # Check that the inserted node was set as the next node for
    # the previous one
    assert nonemptyList.getFirstNode().getNextNode().getValue() == 4

@pytest.mark.insertAfter
# insertAfter functionality for a DoublyLinkedList
def test_dll_insertafter_notlast_next(nonemptyList):
    # Insert a new value as the second element of the list
    nonemptyList.insertAfter(4, 3)
    # Check that the inserted value's next node was set to
    # the node after
    assert nonemptyList.getFirstNode().getNextNode().getNextNode().getValue() == 2

@pytest.mark.insertAfter
# insertAfter functionality for a DoublyLinkedList
def test_dll_insertafter_notlast_previous(nonemptyList):
    # Insert a new value as the second element of the list
    nonemptyList.insertAfter(4, 3)
    # Check that the inserted value's previous node was set to
    # the correct value
    assert nonemptyList.getFirstNode().getNextNode().getPreviousNode().getValue() == 3

@pytest.mark.insertAfter
# insertAfter functionality for a DoublyLinkedList
def test_dll_insertafter_notlast_nextprev(nonemptyList):
    # Insert a new value as the second element of the list
    nonemptyList.insertAfter(4, 3)
    # Check that the inserted node was set as the previous node
    # for the next node
    assert nonemptyList.getFirstNode().getNextNode().getNextNode().getPreviousNode().getValue() == 4

####
# deleteFirstNode
####

@pytest.mark.deleteFirstNode
# deleteFirstNode functionality for a DoublyLinkedList
def test_dll_deletefirstnode_oneitem_val(emptyList):
    # Insert a new node to the list
    emptyList.insertFront(1)
    # Delete the inserted node
    val = emptyList.deleteFirstNode()
    # Check that the value of the deleted node is as expected
    assert val == 1

@pytest.mark.deleteFirstNode
def test_dll_deletefirstnode_oneitem_first(emptyList):
    # Insert a new node to the list
    emptyList.insertFront(1)
    # Delete the inserted node
    emptyList.deleteFirstNode()
    # Check that the first node of the list was set to None
    assert emptyList.getFirstNode() == None

@pytest.mark.deleteFirstNode
def test_dll_deletefirstnode_prev(nonemptyList):
    # Delete the first
    nonemptyList.deleteFirstNode()
    # Check that the next node's previous was set to None
    assert nonemptyList.getFirstNode().getPreviousNode() == None

@pytest.mark.deleteFirstNode
def test_dll_deletefirstnode_first(nonemptyList):
    # Delete the first
    nonemptyList.deleteFirstNode()
    # Check that the first node of the list was set to the next one
    assert nonemptyList.getFirstNode().getValue() == 2

####
# deleteLastNode
####
    
@pytest.mark.deleteLastNode
# deleteLastNode functionality for a DoublyLinkedList
def test_dll_deletelastnode_oneitem_val(emptyList):
    # Insert a new node to the list
    emptyList.insertFront(1)
    # Delete the inserted node
    val = emptyList.deleteLastNode()
    # Check that the value of the deleted node is as expected
    assert val == 1

@pytest.mark.deleteLastNode
# deleteLastNode functionality for a DoublyLinkedList
def test_dll_deletelastnode_oneitem_last(emptyList):
    # Insert a new node to the list
    emptyList.insertFront(1)
    # Delete the inserted node
    val = emptyList.deleteLastNode()
    # Check that the last node of the list was set to None
    assert emptyList.getLastNode() == None

@pytest.mark.deleteFirstNode
def test_dll_deletelastnode_prev(nonemptyList):
    # Delete the last node
    nonemptyList.deleteLastNode()
    # Check that the previous node's next was set to None
    assert nonemptyList.getLastNode().getNextNode() == None

@pytest.mark.deleteLastNode
def test_dll_deletelastnode_first(nonemptyList):
    # Delete the last
    nonemptyList.deleteLastNode()
    # Check that the last node of the list was set to the previous one
    assert nonemptyList.getLastNode().getValue() == 2

####
# deleteValue
####
    
@pytest.mark.deleteValue
# deleteValue functionality for a DoublyLinkedList
def test_dll_deletevalue_val(nonemptyList):
    # Delete the value from the list
    val = nonemptyList.deleteValue(2)
    # Check that the value of the deleted node is as expected
    assert val == 2

@pytest.mark.deleteValue
# deleteValue functionality for a DoublyLinkedList
def test_dll_deletevalue_next(nonemptyList):
    # Delete the value from the list
    nonemptyList.deleteValue(2)
    # Check that the previous node's next node was set
    # as expected
    assert nonemptyList.getFirstNode().getNextNode().getValue() == 1

@pytest.mark.deleteValue
# deleteValue functionality for a DoublyLinkedList
def test_dll_deletevalue_prev(nonemptyList):
    # Delete the value from the list
    nonemptyList.deleteValue(2)
    # Check that the next node's previous node was set
    # as expected
    assert nonemptyList.getLastNode().getPreviousNode().getValue() == 3

####
# forwardTraverse
####

@pytest.mark.forwardTraverse
# forwardTraverse functionality for a DoublyLinkedList
def test_dll_forwardtraverse(nonemptyList, capfd):
    # Print each item in the list
    nonemptyList.forwardTraverse()
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output matches what is expected
    assert out == "3\n2\n1\n"

####
# reverseTraverse
####

@pytest.mark.reverseTraverse
# reverseTraverse functionality for a DoublyLinkedList
def test_dll_reversetraverse(nonemptyList, capfd):
    # Print each item in the list in reverse order
    nonemptyList.reverseTraverse()
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output matches what is expected
    assert out == "1\n2\n3\n"

####
# __len__
####

@pytest.mark.len
# __len__ functionality for a DoublyLinkedList
def test_dll_len(nonemptyList):
    # Check that the len of the list is correct
    assert len(nonemptyList) == 3

####
# __str__
####

@pytest.mark.str
# __str__ functionality for a DoublyLinkedList
def test_dll_str(nonemptyList, capfd):
    # Print the list
    print(nonemptyList)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output is in the expected format
    assert out == "[3 <-> 2 <-> 1]\n"