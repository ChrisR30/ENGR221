import pytest

from ..SearchStructures import Stack, Queue 

#####
# Stack tests
#####

# Stack isEmpty() functionality for empty stack
@pytest.mark.stack
def test_stack_isempty():
    # Create a new stack
    s = Stack()
    # isEmpty() should return true
    assert s.isEmpty()

# Stack add() and isEmpty() functionality
@pytest.mark.stack 
def test_stack_add_notempty():
    # Create new stack
    s = Stack()
    # Add an item to the stack
    s.add("Hello")
    # isEmpty() should return false
    assert not s.isEmpty()

# Stack add() and remove() functionality
@pytest.mark.stack
def test_stack_add_remove():
    # Create new stack
    s = Stack()
    # Add an item to the stack
    s.add("Hello")
    # Remove the item from the stack
    s.remove()
    # isEmpty() should return true
    assert s.isEmpty()

# Check that Stack adds and removes in FILO order
@pytest.mark.stack
def test_stack_order():
    # Create new stack
    s = Stack()
    # Add five items to the stack
    for i in range(5):
        s.add(i)
    items_removed = []
    # Remove items from the stack
    while not s.isEmpty():
        items_removed.append(s.remove())
    # Check that items were removed in FILO order
    assert items_removed == [4, 3, 2, 1, 0]

#####
# Queue tests
#####

# Queue isEmpty() functionality for empty queue
@pytest.mark.queue
def test_queue_isempty():
    # Create a new queue
    q = Queue()
    # isEmpty() should return true
    assert q.isEmpty()

# Queue add() and isEmpty() functionality
@pytest.mark.queue
def test_queue_add_notempty():
    # Create new queue
    q = Queue()
    # Add an item to the queue
    q.add("Hello")
    # isEmpty() should return false
    assert not q.isEmpty()

# Queue add() and remove() functionality
@pytest.mark.queue
def test_queue_add_remove():
    # Create new stack
    q = Queue()
    # Add an item to the queue
    q.add("Hello")
    # Remove the item from the queue
    q.remove()
    # isEmpty() should return true
    assert q.isEmpty()

# Check that Queue adds and removes in FIFO order
@pytest.mark.queue
def test_queue_order():
    # Create new queue
    q = Queue()
    # Add five items to the queue
    for i in range(5):
        q.add(i)
    items_removed = []
    # Remove items from the queue
    while not q.isEmpty():
        items_removed.append(q.remove())
    # Check that items were removed in FIFO order
    assert items_removed == [0, 1, 2, 3, 4]