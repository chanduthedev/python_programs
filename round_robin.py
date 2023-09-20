# Get a string by appending characters in round robin order from a given list of strings.
# l = ['ABC', 'D', 'EF'] => [A, D, E, B, F, C]

l = ["ABC", "D", "EF"]


def find_round_robin_str(str_list: list) -> str:
    # empty check
    if not str_list:
        return ""
    # Get max string length from the list of strings
    max_len = max([len(char) for char in str_list])

    # to store letters in round robin order
    final_list = []
    # repeat until max string length times
    for i in range(max_len):
        for string in str_list:
            if len(string) > i:
                final_list.append(string[i])
    return "".join(final_list)


if __name__ == "__main__":
    print(find_round_robin_str(["ABC", "D", "EF"]))


def test_find_round_robin_str_return_string():
    expected = "ADEBFC"
    actual = find_round_robin_str(["ABC", "D", "EF"])
    assert expected == actual


def test_find_round_robin_str_empty_str_for_empty_list():
    expected = ""
    actual = find_round_robin_str([])
    assert expected == actual


def test_find_round_robin_same_str_for_one_list_item():
    expected = "test"
    actual = find_round_robin_str(["test"])
    assert expected == actual


def test_find_round_robin_same_str_for_unequl_items():
    expected = "ttreeossuttnidnrgoubin"
    actual = find_round_robin_str(["test", "testing", "roundroubin"])
    assert expected == actual
