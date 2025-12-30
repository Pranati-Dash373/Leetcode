'''
Docstring for Majority_element_II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109

'''

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        res =[]
        count1 ,count2 = 0 , 0
        element1 , element2 = None , None
        for i in nums:
            if count1 == 0 and i != element2 :
                count1 = count1 + 1
                element1 = i
            elif count2 == 0 and i != element1 :
                count2 = count2 + 1
                element2 = i
            elif element1 == i:
                count1 += 1
            elif element2 == i:
                count2 += 1
            else:
                count1 =count1 - 1
                count2 =count2 - 1
        for key in (element1,element2):
            if nums.count(key) >  len(nums)//3:
                res.append(key)
        return res