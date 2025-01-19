from src.easy.roman_to_integer import Solution


class TestRomanToInteger:
    def test_basic_cases(self):
        assert Solution().roman_numeral_to_int("III") == 3
        assert Solution().roman_numeral_to_int("IV") == 4
        assert Solution().roman_numeral_to_int("IX") == 9

    def test_larger_cases(self):
        assert Solution().roman_numeral_to_int("LVIII") == 58
        assert Solution().roman_numeral_to_int("MCMXCIV") == 1994
        assert Solution().roman_numeral_to_int("MMXXI") == 2021
        assert Solution().roman_numeral_to_int("MMXX") == 2020
        assert Solution().roman_numeral_to_int("MMXIX") == 2019
