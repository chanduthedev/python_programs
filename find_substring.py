# Problem Statement: Check sub string letters present in the same order in the main string or not

# Sample1:
# Input main_str: abcdefglsyionghdfdfjki, substring: dfj
# Output : Yes

# Sample2:
# Input main_str: Musk Melon,  substring: elm
# Output : No


def is_substr_found(main_str: str, sub_str: str) -> bool:
    """_summary_

    Args:
        main_str (str): main string
        sub_str (str): sub string to be searched in main string

    Returns:
        bool: return true if sub string found in main string otherwise false
    """
    if not main_str and not sub_str:
        return True
    substr_index = 0
    is_found = False
    for index, item in enumerate(main_str):
        if substr_index < len(sub_str) and main_str[index] == sub_str[substr_index]:
            substr_index = substr_index + 1
        if len(sub_str) <= substr_index:
            is_found = True
            break

    return is_found


def test_is_substr_found_should_return_true():
    expected = True
    actual = is_substr_found("abcdefglsyionghdfdfjki", "dfj")
    assert actual == expected


def test_is_substr_found_should_return_true_for_corner_case():
    expected = True
    actual = is_substr_found("Jackfruit", "Jft")
    assert actual == expected


def test_is_substr_found_should_return_false():
    expected = False
    actual = is_substr_found("Musk Melon", "elm")
    assert actual == expected


def test_is_substr_found_should_return_false_for_empty_main_str():
    expected = False
    actual = is_substr_found("", "Jft")
    assert actual == expected


def test_is_substr_found_should_return_true_for_empty_sub_str():
    expected = True
    actual = is_substr_found("Jft", "")
    assert actual == expected


def test_is_substr_found_should_return_true_for_both_empty():
    expected = True
    actual = is_substr_found("", "")
    assert actual == expected
