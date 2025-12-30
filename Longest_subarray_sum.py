'''
Docstring for Longest_subarray_sum

Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

Examples
Example 1:
Input Format: N = 3, k = 5, array[] = {2,3,5}
Result: 2
Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.

Example 2:
Input Format: N = 3, k = 1, array[] = {-1, 1, 1}
Result: 3
Explanation: The longest subarray with sum 1 is {-1, 1, 1}. And its length is 3.


'''

class Solution:
    def longestSubarrayPosNeg(self , nums: list[int] , k: int) -> int:
        sum = 0
        set = {}     
        max_len = 0
        for i in range(len(nums)):
            sum = sum + nums[i]

            if sum == k:
                max_len = max(max_len, i + 1)

            if (sum - k) in set:
                length = i - set[sum - k]
                max_len = max(max_len, length)

            if sum not in set:
                set[sum] = i

        return max_len
