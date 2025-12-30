'''
Docstring for Majority_element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
The input is generated such that a majority element will exist in the array.

'''

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d = {}
        for i  in nums :
            if(i not in d):
                d[i] = 1
            else:
                d[i] = d[i] + 1
        max = 0
        ans = 0
        for i in d.keys():
            if (d[i] > max):
                max = d[i]
                ans = i 
        return ans
