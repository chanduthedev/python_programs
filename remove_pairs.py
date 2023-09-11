# Given a string of letters from alphabet,
# Remove all pairs(2 consecutive same character) of characters which occur
# consecutively and continue till no such pairs exist.

# Solve this problem recursively in O(N) time

# Sample 1:
# i/o: abcdaadhhhhhzppzl
# o/p : abchl

# Sample 2:
# i/p : abcd
# o/p : abcd

# Sample 2:
# i/p : hhhbh
# o/p : hbh


# i/p : abnnbazaxcd
# o/p : zaxcd


#  Implementation
remaining_letters = []


def remove_pair(input_str):
    # when length is one, stop processing
    if len(input_str) == 1:
        remaining_letters.append(input_str[0])
        return input_str
    # append first letter to the remaining list
    if not remaining_letters:
        remaining_letters.append(input_str[0])
    else:
        # remove last element from the list if first letter,
        #  and last letter in the list are same
        if input_str[0] == remaining_letters[-1]:
            remaining_letters.pop()
        else:
            # append first letter to the remaining list
            remaining_letters.append(input_str[0])
    # first letter processed, so call method recursively from second char
    return remove_pair(input_str[1:])


if __name__ == "__main__":
    remove_pair("abcdaadhhhhhzppzl")
    print("".join(remaining_letters))
