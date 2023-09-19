# Example 1:
# input: word = "a123bc34d8ef34"

# [123, 34, 8, 34]
# len([123, 34, 8])


def find_ints_in_str(word: str) -> list:
    ints_list = []
    temp_int_value = 0
    for char in word:
        # print(type(char), char)
        try:
            int_value = int(char)
            temp_int_value = temp_int_value * 10 + int_value
        except Exception:
            if temp_int_value:
                ints_list.append(temp_int_value)
                temp_int_value = 0
                # continue

    # This check is for last char in the word
    if temp_int_value:
        ints_list.append(temp_int_value)
    return ints_list


if __name__ == "__main__":
    find_ints_in_str("a123bc34d8ef34")


def test_find_ints_in_str_return_empty_list_for_only_chars():
    expected = []
    actual = find_ints_in_str("abcd")
    assert expected == actual


def test_find_ints_in_str_return_one_item_list_for_all_digits():
    expected = [12345677]
    actual = find_ints_in_str("12345677")
    assert expected == actual


def test_find_ints_in_str_return_one_item_list_for_all_digits_starting_zero():
    expected = [12345677]
    actual = find_ints_in_str("012345677")
    assert expected == actual


def test_find_ints_in_str_return_one_item_list_for_all_digits_ending_zero():
    expected = [123456770]
    actual = find_ints_in_str("0123456770")
    assert 1 == len(actual) and expected == actual


def test_find_ints_in_str_return_three_item_list_for_string_with_ints():
    expected = [123, 34, 8, 34]
    actual = find_ints_in_str("a123bc34d8ef34")
    assert 4 == len(actual) and expected == actual


def test_find_ints_in_str_return_three_item_list_for_string_start_zero_ints():
    expected = [1, 1, 1]
    actual = find_ints_in_str("a1b01c001")
    assert 3 == len(actual) and expected == actual


def test_find_ints_in_str_return_list_for_string_start_end_zero_ints():
    expected = [1, 12434, 1001]
    actual = find_ints_in_str("a1b12434c001001adfsfsf")
    assert expected == actual


def test_find_ints_in_str_return_list_for_alternative_char_ints():
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 7]
    actual = find_ints_in_str("1a2b3c4d5e6f7h8j9k0r4h7j0")
    print(actual)
    assert expected == actual
