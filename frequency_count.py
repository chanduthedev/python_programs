# Given a string, find the most frequently occurring character and
# 2nd most frequently occurring character and print the corresponding counts
# Example: "XYZABCXXXY"
# Output: X -> 4, Y -> 2


def first_two_largest_key_count(input_str):
    key_count_map = {}
    # creating dictionary with letter:letter_count
    for char in input_str:
        count = key_count_map.get(char, 0)
        key_count_map[char] = count + 1

    # sort map basing on the count and store in the list
    sorted_items = sorted(key_count_map.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:2]


if __name__ == "__main__":
    print(first_two_largest_key_count("aabbaacccdddeee"))


def test_first_two_largest_key_count_happy_path():
    expected = [("a", 4), ("c", 3)]
    actual = first_two_largest_key_count("aabbaacccdddeee")
    assert expected == actual


def test_first_two_largest_key_count_repeat_single_letter_in_string():
    expected = [("a", 5)]
    actual = first_two_largest_key_count("aaaaa")
    assert expected == actual


def test_first_two_largest_key_count_empty_string():
    expected = []
    actual = first_two_largest_key_count("")
    assert expected == actual
