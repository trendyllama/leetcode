
from src.easy.remove_dupes_from_sorted_array import Solution


def test_example_1():
    '''
    Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
    '''


    assert Solution().removeDuplicates([1, 1, 2]) == (2, [1, 2, 0])


def test_example_2():
    '''

   Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    '''

    assert Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == (5, [0,1,2,3,4,0,0,0,0,0])