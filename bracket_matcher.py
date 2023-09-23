# Return true if matching brackets( '(' and ')') in the given string
# and false if not
def bracket_matcher(input_str: str) -> bool:
    remaining_brackets = []
    brackets = ["(", ")"]

    for ch in input_str:
        if remaining_brackets and ((ch == ")" and "(" == remaining_brackets[-1])):
            remaining_brackets.pop()
        elif ch in brackets:
            remaining_brackets.append(ch)

    if remaining_brackets:
        return False
    return True


if __name__ == "__main__":
    print(bracket_matcher("the color re(d))()(()"))
    print(bracket_matcher(")("))


# Input string with balanced brackets
def test_input_string_with_balanced_brackets():
    assert bracket_matcher("()") is True
    assert bracket_matcher("(())") is True
    assert bracket_matcher("((()))") is True
    assert bracket_matcher("()()") is True
    assert bracket_matcher("()()(()())") is True
    assert bracket_matcher("(())()") is True


# Input string with no brackets
def test_input_string_with_no_brackets():
    assert bracket_matcher("") is True
    assert bracket_matcher("abc") is True
    assert bracket_matcher("123") is True
    assert bracket_matcher(" ") is True


# Input string with only one pair of brackets
def test_input_string_with_only_one_pair_of_brackets():
    assert bracket_matcher("()") is True
    assert bracket_matcher("( )") is True
    assert bracket_matcher("(abc)") is True
    assert bracket_matcher("(123)") is True


# Input string with unbalanced brackets
def test_input_string_with_unbalanced_brackets():
    assert bracket_matcher("(") is False
    assert bracket_matcher(")") is False
    assert bracket_matcher(")(") is False
    assert bracket_matcher("())(") is False
    assert bracket_matcher("((())") is False
    assert bracket_matcher("(()()())((()()())") is False


# Input string with only one opening bracket
def test_input_string_with_only_one_opening_bracket():
    assert bracket_matcher("(") is False
    assert bracket_matcher("()(") is False
    assert bracket_matcher("(abc") is False
    assert bracket_matcher("(123") is False


# Input string with only one closing bracket
def test_input_string_with_only_one_closing_bracket():
    assert bracket_matcher(")") is False
    assert bracket_matcher(")(") is False
    assert bracket_matcher("abc)") is False
    assert bracket_matcher("123)") is False
