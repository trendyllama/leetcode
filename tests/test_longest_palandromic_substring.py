'''
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

'''
from src.easy.longest_palandromic_substring import is_palandrome, get_largest_palandrome

def test_is_palandrome():

    assert is_palandrome("babad") is False
    assert is_palandrome("cbbd") is False
    assert is_palandrome("racecar")
    assert is_palandrome("a")
    assert is_palandrome("ab") is False
    assert is_palandrome("abc") is False
    assert is_palandrome("level")
    assert is_palandrome("noon")
    assert is_palandrome("radar")
    assert is_palandrome("refer")
    assert is_palandrome("repaper")
    assert is_palandrome("aibohphobia")


def test_get_largest_palandrome():

    assert get_largest_palandrome("babad") == "bab" or get_largest_palandrome("babad") == "aba"
    assert get_largest_palandrome("cbbd") == "bb"