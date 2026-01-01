'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

'''

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)
        def merge_array(l1: int, m: int, l2: int, n: int) -> list[int]:
            l = []
            i,j = 0, 0
            while(i<m and j<n):
                if l1[i]<= l2[j]:
                    l.append(l1[i])
                    i+=1
                else:
                    l.append(l2[j])
                    j+=1
            if m<=n:
                l = l + l2[j:]
            if n<=m:
                l = l + l1[i:]
            return l
        merged_list = merge_array(nums1, m, nums2, n)
        if m+n == 1:
            return float(merged_list[0])
        if (m+n) % 2 != 0:
            return float(merged_list[((m+n-1)//2)])
        else:
            i = (m+n)//2
            j = i+1
            print(m,n,i,j, merged_list[i-1], merged_list[j-1])
            return float((merged_list[i-1]+merged_list[j-1])/2)
