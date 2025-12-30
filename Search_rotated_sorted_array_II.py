'''
Docstring for Search_rotated_sorted_array_II

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
 
'''

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        l = 0
        h = n-1
        while (l <= h):
            mid = l + ((h - l )//2)
            if (nums[mid] == target):
                return True
            if (nums[l] == nums[mid] and nums[mid] == nums[h]):
                l += 1
                h -= 1
                continue
            if (nums[l] <= nums[mid]):
                if (nums[l] <= target and target <= nums[mid]):
                    h = mid - 1
                else:
                    l = mid + 1

            else:
                if (nums[mid] <= target and target <= nums[h]):
                    l = mid + 1
                else:
                    h = mid - 1
        return  False
