# Find list of sequence of lists from the given list of integers and
# return empty if no sequence numbers in the given list


def find_seq_sub_list(input_list: list) -> list[list]:
    sub_list = []
    final_list = []
    for item in input_list:
        sub_list_len = len(sub_list)
        if not sub_list:
            sub_list.append(item)
        elif sub_list_len > 0 and item - 1 == sub_list[sub_list_len - 1]:
            sub_list.append(item)
        else:
            # Sequence break and adding current sequence list to main list
            if sub_list_len > 1:
                final_list.append(sub_list)
            # Start new list
            sub_list = [item]

    # final sublist after the loop end
    if len(sub_list) > 1:
        final_list.append(sub_list)
    return final_list


if __name__ == "__main__":
    print(find_seq_sub_list([1, 2, 3, 6, 8, 9, 5, 6]))


def test_find_seq_sub_list_return_list_of_lists():
    expected = [[1, 2, 3], [8, 9], [5, 6]]
    actual = find_seq_sub_list([1, 2, 3, 6, 8, 9, 5, 6])
    assert actual == expected


def test_find_seq_sub_list_return_empty_list():
    expected = []
    actual = find_seq_sub_list([1, 3, 6, 8, 5, 10])
    assert actual == expected


def test_find_seq_sub_list_return_empty_list_for_empty_input():
    expected = []
    actual = find_seq_sub_list([])
    assert actual == expected


def test_find_seq_sub_list_return_one_item_list_for_sequence_numbers():
    expected = [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]]
    actual = find_seq_sub_list([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
    assert actual == expected
