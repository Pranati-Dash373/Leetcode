'''
Docstring for Set_matrix_zero

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1

'''

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n =len(matrix)
        m = len(matrix[0])
        col0 = 1
        row0 =1
        for j in range(m):
            if matrix[0][j] == 0:
                row0 = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] ==0:
                    matrix[i][0] = 0
                    if (j != 0):
                        matrix[0][j] = 0
                    else:
                        col0 = 0
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]!= 0:
                    if(matrix[i][0] == 0 or matrix[0][j] == 0):
                        matrix[i][j] = 0
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0
        if row0 == 0:
            for j in range(m):
                matrix[0][j] = 0
        return matrix

