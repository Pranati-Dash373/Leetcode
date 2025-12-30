'''
Docstring for Find_peak_element_II

A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

 

Example 1:



Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.
Example 2:



Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 500
1 <= mat[i][j] <= 105
No two adjacent cells are equal.

'''

class Solution:
    def maxElement(self , mat:list[list[int]] , n: int ,m:int , mid: int) ->list[int]:
        max_element = -1
        index = -1
        for i in range(n):
            if (mat[i][mid] > max_element):
                max_element = mat[i][mid]
                index = i
        return index

    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m-1
        while(low <= high):
            mid = low + ((high - low ) // 2)
            row = self.maxElement(mat , n ,m , mid)
            left = mat[row][mid-1] if  mid -1 >= 0 else -1
            right = mat[row][mid+1] if mid +1 < m else -1
            if (mat[row][mid] > left and mat[row][mid] > right ):
                return (row , mid)
            elif(mat[row][mid] < left):
                high = mid - 1
            else:
                low = mid + 1
        return (-1 , -1)


