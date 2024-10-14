"""Testing functions from utils file."""

__author__ = "730670853"

from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_notinmod2() -> None:
    """List of only odd numbers: 1, 3, 5"""
    assert only_evens([1, 3, 5]) == []


def test_only_evens_inmod2() -> None:
    """List of only even numbers: 2, 4 ,6"""
    assert only_evens([2, 4, 6]) == [2, 4, 6]


def test_only_evens_emptylist() -> None:
    """List is empty"""
    assert only_evens([]) == []


def test_sub_setcard3ofints() -> None:
    """Initial int set of cardinality 3, taking a subset from idx 0 to 1"""
    assert sub([7, 9, 10], 0, 2) == [7, 9]


def test_sub_setcard5ofints() -> None:
    """Initial int set of cardinality 5, taking a subset from idx 2 to 4"""
    assert sub([1, 3, 7, 30, 97], 2, 5) == [7, 30, 97]


def test_sub_negativeidx() -> None:
    """Initial int set of cardinality 5, end is 4, but idx is negative 1"""
    assert sub([1, 2, 3, 4, 5], -1, 5) == [1, 2, 3, 4, 5]


def test_add_at_index_card3intset_atidx1() -> None:
    """Initial int set of cardinality 3, inserting an int at idx 1"""
    list1: list[int] = [1, 4, 3]
    add_at_index(list1, 5, 1)
    assert list1 == [1, 5, 4, 3]


def test_add_at_index_card5intsent_atidx3() -> None:
    """Initial int set of cardinality 5, inserting an int at idx 3"""
    list2: list[int] = [2, 4, 7, 9, 40]
    add_at_index(list2, 55, 3)
    assert list2 == [2, 4, 7, 55, 9, 40]


def test_add_at_index_idxtoobig() -> None:
    """Initial int set is the empty set"""
    list3 = []
    add_at_index(list3, 1, 0)
    assert list3 == [1]
