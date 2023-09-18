# iterate string
# insert each character in dictionary
# if available decrease/increase basing on value
# iterate dictionary for validation
# .  if input string even, no letter should greater than 0
# for odd all letters should be 1
def become_pallindrome(input_str: str) -> bool:
    if not input_str or len(input_str) < 2:
        return True
    key_count_map = {}
    for char in input_str:
        key_count = key_count_map.get(char, 0)
        if not key_count:
            key_count_map[char] = key_count + 1
        else:
            key_count_map[char] = key_count - 1
    list_values = list(set(key_count_map.values()))
    if len(list_values) == 1 and 0 in list_values:
        # print("Become palindrome")
        return True
    if (len(list_values) == 2) and ([0, 1] == list_values):
        return True
    return False


if __name__ == "__main__":
    become_pallindrome("abcabc")


def test_become_pallindrome_should_be_pallindrome():
    expected = True
    actual = become_pallindrome("abcbc")
    assert expected == actual


def test_become_pallindrome_should_not_be_pallindrome():
    expected = False
    actual = become_pallindrome("abc")
    assert expected == actual


def test_become_pallindrome_single_letter_be_pallindrome():
    expected = True
    actual = become_pallindrome("a")
    assert expected == actual


def test_become_pallindrome_long_str_be_pallindrome():
    expected = True
    actual = become_pallindrome("chanduthedevchanduthedev")
    assert expected == actual
