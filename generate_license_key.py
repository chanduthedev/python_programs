from secrets import token_hex


def generate_part() -> str:
    """Generate 8 character alphanumeric string

    Returns:
        str: Generated 8 letter alphanumeric string
    """
    return token_hex(4)


def generate_license_key() -> str:
    """Generate a license key

    Returns:
        str: generated license key
    """
    return "-".join(generate_part() for _ in range(4))


if __name__ == "__main__":
    print(generate_license_key())


# Generate a license key with 4 parts of 8 alphanumeric characters separated by hyphens
def test_generate_license_key_with_4_parts():
    license_key = generate_license_key()
    parts = license_key.split("-")
    assert len(parts) == 4
    for part in parts:
        print(part)
        assert len(part) == 8
        assert part.isalnum()
        assert part.islower() or part.isupper()


# Generate multiple license keys without errors
def test_generate_multiple_license_keys():
    for _ in range(10):
        license_key = generate_license_key()
        assert license_key


# Generate a license key with only letters
def test_generate_license_key_with_only_letters():
    license_key = generate_license_key()
    parts = license_key.split("-")
    assert len(parts) == 4
    for part in parts:
        assert len(part) == 8
        assert part.islower() or part.isupper()


# Generate a license key with empty parts
def test_generate_license_key_with_empty_parts():
    license_key = generate_license_key()
    parts = license_key.split("-")
    assert len(parts) == 4
    for part in parts:
        assert len(part) == 8
        assert part


# Generate a license key with non-alphanumeric characters
def test_generate_license_key_with_non_alphanumeric_characters():
    license_key = generate_license_key()
    parts = license_key.split("-")
    assert len(parts) == 4
    for part in parts:
        assert len(part) == 8
        assert not part.isalpha() or not part.isnumeric()


# Generate a license key with less than 4 parts
def test_generate_license_key_with_less_than_4_parts():
    license_key = generate_license_key()
    parts = license_key.split("-")
    assert len(parts) == 4
