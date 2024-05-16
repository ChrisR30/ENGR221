import pytest

from ..deque import Deque 

@pytest.fixture 
# Define an empty Deque for testing
def emptyDeque():
    return Deque()

@pytest.fixture 
# Define a Deque for testing
# Should look like [3 <-> 2 <-> 1]
def nonemptyDeque():
    d = Deque()
    d.insertLeft(1)
    d.insertLeft(2)
    d.insertLeft(3)
    return d

####
# isEmpty
####

@pytest.mark.isEmpty 
# isEmpty functionality for a Deque
def test_deque_isempty_true(emptyDeque):
    # isEmpty should return True
    assert emptyDeque.isEmpty()

@pytest.mark.isEmpty 
# isEmpty functionality for a Deque
def test_deque_isempty_false(nonemptyDeque):
    # isEmpty should return False
    assert not nonemptyDeque.isEmpty()

####
# __len__
####

@pytest.mark.len
# __len__ functionality for a Deque
def test_deque_len(nonemptyDeque):
    # Check that the len of the deque is correct
    assert len(nonemptyDeque) == 3

####
# __str__
####

@pytest.mark.str
# __str__ functionality for a Deque
def test_deque_str(nonemptyDeque, capfd):
    # Print the deque
    print(nonemptyDeque)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output is in the expected format
    assert out == "[3 <-> 2 <-> 1]\n"

####
# peekLeft
####

@pytest.mark.peekLeft
# peekLeft functionality for a Deque
def test_deque_peekleft(nonemptyDeque):
    # Check that we are checking the first (leftmost) node
    assert nonemptyDeque.peekLeft() == 3

####
# peekRight
####

@pytest.mark.peekRight
# peekRight functionality for a Deque
def test_deque_peekright(nonemptyDeque):
    # Check that we are checking the last (rightmost) node
    assert nonemptyDeque.peekRight() == 1

####
# insertLeft
####

@pytest.mark.insertLeft
# insertLeft functionality for a Deque
def test_deque_insertleft_len(nonemptyDeque):
    # Insert an item to the left of the deque
    nonemptyDeque.insertLeft(4)
    # Check that the deque has an additional item
    assert len(nonemptyDeque) == 4

@pytest.mark.insertLeft
# insertLeft functionality for a Deque
def test_deque_insertleft_value(nonemptyDeque):
    # Insert an item to the left of the deque
    nonemptyDeque.insertLeft(4)
    # Check that the deque has an additional item
    assert nonemptyDeque.peekLeft() == 4

####
# insertRight
####

@pytest.mark.insertRight
# insertRight functionality for a Deque
def test_deque_insertright_len(nonemptyDeque):
    # Insert an item to the right of the deque
    nonemptyDeque.insertRight(4)
    # Check that the deque has an additional item
    assert len(nonemptyDeque) == 4

@pytest.mark.insertRight
# insertRight functionality for a Deque
def test_deque_insertright_value(nonemptyDeque):
    # Insert an item to the right of the deque
    nonemptyDeque.insertRight(4)
    # Check that the deque has an additional item
    assert nonemptyDeque.peekRight() == 4

####
# removeLeft
####

@pytest.mark.removeLeft
# removeLeft functionality for a Deque
def test_deque_removeleft_len(nonemptyDeque):
    # Remove an item from the left of the deque
    nonemptyDeque.removeLeft()
    # Check that the deque has one less item
    assert len(nonemptyDeque) == 2

@pytest.mark.removeLeft
# removeLeft functionality for a Deque
def test_deque_removeleft_val(nonemptyDeque):
    # Remove an item from the left of the deque
    val = nonemptyDeque.removeLeft()
    # Check that the removed value was as expected
    assert val == 3

####
# removeRight
####

@pytest.mark.removeRight
# removeRight functionality for a Deque
def test_deque_removeright_len(nonemptyDeque):
    # Remove an item from the right of the deque
    nonemptyDeque.removeRight()
    # Check that the deque has one less item
    assert len(nonemptyDeque) == 2

@pytest.mark.removeRight
# removeRight functionality for a Deque
def test_deque_removeright_val(nonemptyDeque):
    # Remove an item from the right of the deque
    val = nonemptyDeque.removeRight()
    # Check that the removed value was as expected
    assert val == 1