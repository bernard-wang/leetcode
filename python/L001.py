"""
Description:
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Constrains:
* 2 <= nums.length <= 10^4
* -10^9 <= nums[i] <= 10^9
* -10^9 <= target <= 10^9

Ideas:
1. use a hashmap (dict) to store key-value pairs (num:index), for every num, search for (target - num)
2. sort, then use binary search (this is wrong, because sort would wreck the original indices of nums, unless to return (num1, num2))
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = dict()
        for i, num in enumerate(nums):
            key = target - num
            if key in index:
                return (index[key], i)
            index[key] = i
        return (-1, -1)
