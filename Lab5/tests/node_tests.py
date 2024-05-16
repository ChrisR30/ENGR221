import pytest

from ..doubleNode import DoubleNode

@pytest.fixture 
# Define a DoubleNode for testing
def node(value=5):
    return DoubleNode(value)

####
# isFirst
####

@pytest.mark.isFirst
# isFirst functionality for DoubleNode
def test_doublenode_isfirst_true(node):
    # isFirst should return True
    assert node.isFirst()

@pytest.mark.isFirst
# isFirst functionality for DoubleNode
def test_doublenode_isfirst_false(node):
    # Create a new DoubleNode and set previous
    dn2 = DoubleNode(3, next=None, previous=node)
    # isFirst should return False
    assert not dn2.isFirst()

####
# isLast
####

@pytest.mark.isLast
# isLast functionality for DoubleNode
def test_doublenode_islast_true(node):
    # isLast should return True
    assert node.isLast()

@pytest.mark.isLast
# isLast functionality for DoubleNode
def test_doublenode_islast_false(node):
    # Create a new DoubleNode and set next
    dn2 = DoubleNode(3, next=node, previous=None)
    # isLast should return False
    assert not dn2.isLast()

####
# getValue
####

@pytest.mark.getValue
# getValue functionality for DoubleNode
def test_doublenode_getvalue(node):
    # node has value 5 by default
    assert node.getValue() == 5

####
# getNextNode
####

@pytest.mark.getNextNode
# getNextNode functionality for DoubleNode
def test_doublenode_getnextnode(node):
    # Create a new DoubleNode and set next
    dn2 = DoubleNode(3, next=node, previous=None)
    # Check that dn2's next node was set correctly
    assert dn2.getNextNode() == node

####
# getPreviousNode
####

@pytest.mark.getPreviousNode
# getPreviousNode functionality for DoubleNode
def test_doublenode_getpreviousnode(node):
    # Create a new DoubleNode and set previous
    dn2 = DoubleNode(3, next=None, previous=node)
    # Check that dn2's previous node was set correctly
    assert dn2.getPreviousNode() == node

####
# setValue
####

@pytest.mark.setValue
# setValue functionality for DoubleNode
def test_doublenode_setvalue(node):
    # Change node's value to 3
    node.setValue(3)
    # Check that the new value is correct
    assert node.getValue() == 3

####
# setNextNode
####

@pytest.mark.setNextNode
# setNextNode functionality for DoubleNode 
def test_doublenode_setnextnode(node):
    # Create a new doubleNode
    dn2 = DoubleNode(3)
    # Set node's next to dn2
    node.setNextNode(dn2)
    # Check that the next node was set correctly
    assert node.getNextNode() == dn2 

####
# setPreviousNode
####

@pytest.mark.setPreviousNode
# setPreviousNode functionality for DoubleNode 
def test_doublenode_setpreviousnode(node):
    # Create a new doubleNode
    dn2 = DoubleNode(3)
    # Set node's previous to dn2
    node.setPreviousNode(dn2)
    # Check that the previous node was set correctly
    assert node.getPreviousNode() == dn2 

####
# __str__
####

@pytest.mark.str
# __str__ functionality for DoubleNode
def test_doublenode_str(node, capfd):
    # Print the node
    print(node)
    # Capture the output
    out, _ = capfd.readouterr()
    # Confirm that the output is as expected
    assert out == "5\n"