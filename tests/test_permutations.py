
from src.medium.premutations import Solution

def test_example1():
    '''
    Example 1:

    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    '''

    assert Solution().permute([1, 2, 3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


def test_example2():
    '''
    Example 2:

    Input: nums = [0,1]
    Output: [[0,1],[1,0]]
    '''
    assert Solution().permute([0, 1]) == [[0,1],[1,0]]


def test_example3():
    '''
    Example 3:

    Input: nums = [1]
    Output: [[1]
    '''

    assert Solution().permute([1]) == [[1]]
