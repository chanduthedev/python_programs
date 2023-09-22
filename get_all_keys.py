def get_keys_from_dict(input_map, key_list):
    if isinstance(input_map, dict):
        keys = input_map.keys()
        # Iterate all first level keys in the dict
        for key in keys:
            key_list.append(key)
            temp_map = input_map.get(key, None)
            # iterate again if value is also a dict
            if isinstance(temp_map, dict):
                for key, value in temp_map.items():
                    get_keys_from_dict({key: value}, key_list)
    else:
        return ""


if __name__ == "__main__":
    result_keys = []
    input_list = {1: {2: {3: "hi"}, 4: {5: "Hello"}}}

    get_keys_from_dict(input_list, result_keys)
    print(((result_keys)))


def test_get_keys_from_dict_return_keys_for_simple_dict():
    input_data = {1: "one", 2: "two", 3: "three"}
    result = []
    get_keys_from_dict(input_data, result)
    assert result == [1, 2, 3]


def test_get_keys_from_dict_return_empty_for_empty_dict():
    input_data = {}
    result = []
    get_keys_from_dict(input_data, result)
    assert result == []


def test_get_keys_from_dict_return_keys_for_nested_dict():
    input_data = {1: {2: {3: "hi"}, 4: {5: "Hello"}}}
    result = []
    get_keys_from_dict(input_data, result)
    assert result == [1, 2, 3, 4, 5]


def test_get_keys_from_dict_return_keys_for_complex_dict():
    input_data = {1: {2: {"three": {4: {5: "Hello"}}}}}
    result = []
    get_keys_from_dict(input_data, result)
    assert result == [1, 2, "three", 4, 5]
