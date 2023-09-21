# Find two given strings are anagrams or not


def is_anagram(str1: str, str2: str) -> bool:
    # remove spaces
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # return false if length is not equal
    if len(str1) != len(str2):
        return False

    # Making two maps with char as key and value a its frequency
    str1_dict = str2_dict = {}

    for str1_char, str2_char in zip(str1, str2):
        str1_char_cnt = str1_dict.get(str1_char, 0)
        str1_char_cnt += 1
        str1_dict[str1_char] = str1_char_cnt

        str2_char_cnt = str2_dict.get(str2_char, 0)
        str2_char_cnt += 1
        str2_dict[str2_char] = str2_char_cnt

    return str1_dict == str2_dict


if __name__ == "__main__":
    if is_anagram("a gentleman", "elegant man"):
        print("Given two strings are anagrams to each other")
    else:
        print("Given two strings are not anagrams to each other")


def test_is_anagram_return_true_for_two_sentences():
    expected = True
    actual = is_anagram("a gentleman", "elegant man")
    assert expected == actual


def test_is_anagram_return_true_for_two_strs():
    expected = True
    actual = is_anagram("peach", "cheap")
    assert expected == actual


def test_is_anagram_return_false_for_two_strs():
    expected = False
    actual = is_anagram("chanduthedev", "chandrathedev")
    assert expected == actual


def test_is_anagram_return_true_for_two_empty_strs():
    expected = True
    actual = is_anagram("", "")
    assert expected == actual


def test_is_anagram_return_false_for_one_empty_strs():
    expected = False
    actual = is_anagram("", "chanduthedev")
    assert expected == actual
