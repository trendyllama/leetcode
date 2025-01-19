"""
# Permuations

Given an array nums of distinct integers, return all the possible
permutations
. You can return the answer in any order.

## Example 1

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

## Example 2

Input: nums = [0,1]
Output: [[0,1],[1,0]]


## Example 3

Input: nums = [1]
Output: [[1]]


## Constraints

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

"""

from typing import Callable

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        length_of_input = len(nums)

        init_nums = nums

        permutations = []

        def permute_inner_closure(nums: list[int], num_calls_to_go: int) -> Callable | None:

            if num_calls_to_go < 1:
                return

            for idx, _ in enumerate(nums):
                try:

                    nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]

                    permutations.append(nums)
                except IndexError:
                    continue

            return permute_inner_closure(init_nums, num_calls_to_go-1)

        permute_inner_closure(nums, length_of_input)

        return permutations
