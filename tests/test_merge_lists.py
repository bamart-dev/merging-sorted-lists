import pytest
from main import merge_lists


def test_merge_two_sorted_lists():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    expected = [1, 2, 3, 4, 5, 6]
    assert merge_lists(list1, list2) == expected


def test_merge_with_empty_list():
    list1 = [1, 2, 3]
    list2 = []
    expected = [1, 2, 3]
    assert merge_lists(list1, list2) == expected


def test_merge_two_empty_lists():
    list1 = []
    list2 = []
    expected = []
    assert merge_lists(list1, list2) == expected


def test_merge_lists_with_duplicates():
    list1 = [1, 2, 2, 3]
    list2 = [2, 3, 4]
    expected = [1, 2, 2, 2, 3, 3, 4]
    assert merge_lists(list1, list2) == expected


def test_merge_lists_with_negative_numbers():
    list1 = [-3, -1, 2]
    list2 = [-2, 0, 3]
    expected = [-3, -2, -1, 0, 2, 3]
    assert merge_lists(list1, list2) == expected


def test_merge_lists_with_invalid_chars():
    list1 = [1, 2, 4, 5]
    list2 = ["6"]
    expected = "Merge failed: invalid element present."

    assert merge_lists(list1, list2) == expected
