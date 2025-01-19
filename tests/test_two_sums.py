"""
tests for src/individual_problems/two_sums.py
"""

from src.easy.two_sums import Solution


def test_solution():
    assert Solution().two_sums([3, 2, 4], 6) == [1, 2]
    assert Solution().two_sums([3, 3], 6) == [0, 1]
    assert Solution().two_sums([2, 7, 11, 15], 9) == [0, 1]
