from string_utils import StringUtils

utils = StringUtils()


def test_capitalize_positive():
    assert utils.capitalize("skypro") == "Skypro"


def test_trim_positive():
    assert utils.trim("   skypro") == "skypro"


def test_contains_positive():
    assert utils.contains("SkyPro", "S") is True


def test_delete_symbol_positive():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_capitalize_empty_string():
    assert utils.capitalize("") == ""


def test_trim_no_spaces():
    assert utils.trim("skypro") == "skypro"


def test_contains_negative():
    assert utils.contains("SkyPro", "U") is False


def test_delete_symbol_not_found():
    assert utils.delete_symbol("SkyPro", "U") == "SkyPro"


def test_capitalize_space():
    assert utils.capitalize(" ") == " "


def test_trim_empty_string():
    assert utils.trim("") == ""


def test_contains_space():
    assert utils.contains("Sky Pro", " ") is True


def test_delete_symbol_substring():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
