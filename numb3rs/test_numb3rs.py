from numb3rs import validate

def test_valid_ipv4():
    """Test that perfectly valid IPv4 addresses return True."""
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True
    assert validate("0.0.0.0") is True
    assert validate("192.168.1.1") is True
    assert validate("10.0.0.1") is True


def test_first_byte_only_bug():
    """
    Catches the bug where the code only validates the first byte.
    If the code only checks the first number, these should incorrectly 
    pass as True, but our test expects False.
    """
    assert validate("255.300.300.300") is False
    assert validate("1.256.1.1") is False
    assert validate("127.1.1.500") is False


def test_out_of_range_bytes():
    """Test that any individual byte exceeding 255 returns False."""
    assert validate("256.1.1.1") is False
    assert validate("1.256.1.1") is False
    assert validate("1.1.256.1") is False
    assert validate("1.1.1.256") is False
    assert validate("999.999.999.999") is False


def test_invalid_formats():
    """Test that incorrect structures, lengths, or non-numeric inputs return False."""
    assert validate("cat") is False
    assert validate("1.2.3") is False          # Too few bytes
    assert validate("1.2.3.4.5") is False        # Too many bytes
    assert validate("192.168.1") is False        # Missing last byte
    assert validate("192.168.1.abc") is False    # Contains letters
    assert validate("192.168.1.1.1") is False    # Five bytes

    test_valid_ipv4()
    test_first_byte_only_bug()
    test_out_of_range_bytes()
    test_invalid_formats()