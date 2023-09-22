# Sort a dict basing on nth element of the value,
# consider all the values are lists in the dictionary

output = {"b": [5, 0, 7], "c": [7, 1, 9], "a": [1, 10, 3]}


def dict_custom_sort(input_dict):
    if not input_dict:
        return {}

    # checking list length of each value in the dict
    dict_list = list(input_dict.items())
    list_size = len(dict_list[0][1])
    if list_size < 2:
        raise Exception("List length should be atleast 2.")

    if not all(len(item[1]) == list_size for item in dict_list):
        raise Exception("Length of all list should be equal.")

    for outer, _ in enumerate(dict_list):
        for inner, _ in enumerate(dict_list):
            # e.g: item is (k,[1,2,3]) item[1][1] is 2 as sorting on 2nd item
            if dict_list[inner][1][1] > dict_list[outer][1][1]:
                # swapping
                dict_list[inner], dict_list[outer] = (
                    dict_list[outer],
                    dict_list[inner],
                )

    return dict(dict_list)


if __name__ == "__main__":
    ip_dict = {"a": [1, 10, 3], "b": [5, 0, 7], "c": [7, 1, 9]}
    print(dict_custom_sort(ip_dict))


def test_dict_custom_sort_return_sorted_dict():
    input_dict = {"a": [1, 10, 3], "b": [5, 0, 7], "c": [7, 1, 9]}
    actual = {"b": [5, 0, 7], "c": [7, 1, 9], "a": [1, 10, 3]}
    expected = dict_custom_sort(input_dict)
    assert actual == expected


def test_dict_custom_sort_return_same_dict():
    input_dict = {"a": [1, 1, 3], "b": [5, 2, 7], "c": [7, 3, 9]}
    actual = {"a": [1, 1, 3], "b": [5, 2, 7], "c": [7, 3, 9]}
    expected = dict_custom_sort(input_dict)
    assert actual == expected


def test_dict_custom_sort_return_empty_for_empty_dict():
    input_dict = {}
    actual = {}
    expected = dict_custom_sort(input_dict)
    assert actual == expected


import pytest


def test_dict_custom_sort_exception_for_wrong_length():
    input_dict = {"a": [1, 1, 3], "b": [5, 4], "c": [7, 3, 9]}
    with pytest.raises(Exception, match="Length of all list should be equal."):
        dict_custom_sort(input_dict)


def test_dict_custom_sort_exception_for_less_than_2_length():
    input_dict = {"a": [1], "b": [5, 4], "c": [7, 3, 9]}
    with pytest.raises(Exception, match="List length should be atleast 2."):
        dict_custom_sort(input_dict)
