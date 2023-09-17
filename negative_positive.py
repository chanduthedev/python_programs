# Rearrange list of integers in such way that all  -ve numbers should come first
#  and +ve numbers should come next. Numbers no need to be in sorted order.


# Logic:
# Move left index until +ve
# Move right index until -ve
# swap left and right elements
# Continue until left index cross right index


def arrange_numbers(input_list: list) -> list:
    left = 0
    right = len(input_list) - 1
    while left < right:
        # Move to left until find +ve number
        while left < (len(input_list) - 1) and input_list[left] < 0:
            left = left + 1
        # Move to right until find -ve number
        while right > 0 and input_list[right] > 0:
            right = right - 1
        input_list[left], input_list[right] = input_list[right], input_list[left]
    return input_list


def test_arrange_numbers_return_arranged_list():
    given = [0, -1, 3, -5, -2, 8, 3]
    expected = [-2, -1, -5, 0, 3, 8, 3]
    actual = arrange_numbers(given)
    assert expected == actual


def test_arrange_numbers_return_same_list_for_all_pos_list():
    given = [1, 5, 2]
    expected = [1, 5, 2]
    actual = arrange_numbers(given)
    assert expected == actual


def test_arrange_numbers_return_same_list_for_all_neg_list():
    given = [-1, -5, -2]
    expected = [-1, -5, -2]
    actual = arrange_numbers(given)
    assert expected == actual


def test_arrange_numbers_return_empty_for_empty_list():
    given = []
    expected = []
    actual = arrange_numbers(given)
    assert expected == actual


if __name__ == "__main__":
    print(arrange_numbers([-1, -5, -2]))
