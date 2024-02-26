import pytest

from myset import MySet

@pytest.mark.settest1
def test_init_set(vals=[1, 2, 3]):
    s = MySet(vals)
    assert (s.size() == 3 and set(s.vals()) == set([1, 2, 3]))

@pytest.mark.settest1
def test_init_set_dups(vals=[0, 0, 0, 0]):
    s = MySet(vals)
    assert (s.size() == 1 and set(s.vals()) == set([0]))

@pytest.mark.settest2
def test_search_set(vals=['E', 'N', 'G', 'R', 2, 1]):
    s = MySet(vals)
    assert s.search('E')

@pytest.mark.settest2
def test_search_set_absent(vals=['E', 'N', 'G', 'R', 2, 1]):
    s = MySet(vals)
    assert not s.search(0)

@pytest.mark.settest3
def test_insert_set():
    s = MySet(['E', 'N', 'G', 'R', 2, 1])
    s.insert('!')
    assert (s.size() == 7 and set(s.vals()) == set(['E', 'N', 'G', 'R', 2, 1, '!']))

@pytest.mark.settest3
def test_insert_set_empty():
    s = MySet([])
    s.insert(0)
    assert (s.size() == 1 and set(s.vals()) == set([0]))

@pytest.mark.settest3
def test_insert_set_dups():
    s = MySet(['E', 'N', 'G', 'R', 2, 1])
    s.insert(2)
    assert (s.size() == 6 and set(s.vals()) == set(['E', 'N', 'G', 'R', 2, 1]))

@pytest.mark.settest4
def test_delete_set():
    s = MySet(['E', 'N', 'G', 'R', 2, 1])
    s.delete(2)
    assert (s.size() == 5 and set(s.vals()) == set(['E', 'N', 'G', 'R', 1]))

@pytest.mark.settest4
def test_delete_set_absent():
    s = MySet(['E', 'N', 'G', 'R', 2, 1])
    s.delete(0)
    assert (s.size() == 6 and set(s.vals()) == set(['E', 'N', 'G', 'R', 2, 1]))

@pytest.mark.settest5
def test_traverse_set(capfd):
    s = MySet(['E', 'N', 'G', 'R', 2, 1])
    s.traverse()
    out, err = capfd.readouterr()
    assert out == "E\nN\nG\nR\n2\n1\n"