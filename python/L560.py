"""
Description:
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.
A subarray is a contiguous non-empty sequence of elements within an array.

Constrains:
* 1 <= nums.length <= 2 * 10^4
* -1000 <= nums[i] <= 1000
* -10^(-7) <= k <= 10^7

Ideas:
I can think of keep a prefix sum array, and use a brute-force solution
But the idea is to keep `count` increment every time when the partial sum increases `k`
"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_till_now = 0
        d = {0: 1}
        
        for i in range(len(nums)):
            sum_till_now += nums[i]
            count += d.get(sum_till_now - k, 0)
            d[sum_till_now] = d.get(sum_till_now, 0) + 1
        return count
