def lists_fraction_sort(numers, denoms) -> (list, list):
    # form a list with fraction values
    zip_list = [(item1, item2, item1 / item2) for item1, item2 in zip(numers, denoms)]

    # sort basing on fraction value
    new_list = sorted(zip_list, key=lambda item: item[2])
    sorted_numers = [item[0] for item in new_list]
    sorted_denoms = [item[1] for item in new_list]
    return (sorted_numers, sorted_denoms)


if __name__ == "__main__":
    n = [1, 3, 4, 5, 6]
    d = [1, 2, 3, 4, 6]
    print(lists_fraction_sort(n, d))

import pytest


def test_lists_fraction_sort_return_sorted_list():
    # input data
    numes = [1, 3, 4, 5, 6]
    denoms = [1, 2, 3, 4, 6]

    expected = ([1, 6, 5, 4, 3], [1, 6, 4, 3, 2])

    actual = lists_fraction_sort(numes, denoms)
    assert actual == expected


def test_lists_fraction_sort_return_zero_not_allow_exception():
    # input data
    numes = [1, 3, 4, 5, 6]
    denoms = [1, 2, 0, 4, 6]
    with pytest.raises(Exception, match="Zero not allowed in denominators list."):
        lists_fraction_sort(numes, denoms)


def test_lists_fraction_sort_numes_len_less_return_invalid_len_exception():
    # input data
    numes = [1, 3, 4]
    denoms = [1, 2, 0, 4, 6]
    with pytest.raises(Exception, match="Input lists length should be equal."):
        lists_fraction_sort(numes, denoms)


def test_lists_fraction_sort_numes_len_greater_return_invalid_len_exception():
    # input data
    numes = [1, 3, 4, 1, 4, 5, 6, 7, 8]
    denoms = [1, 2, 0, 4, 6]
    with pytest.raises(Exception, match="Input lists length should be equal."):
        lists_fraction_sort(numes, denoms)
