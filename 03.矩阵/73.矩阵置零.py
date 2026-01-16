from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
    #核心思路：先记录需要清零的行列，而不是边扫描边清零，否则会污染后续的列
    #用第一行保存是否matrix[0][i]当列需要被清零
    #用第一列保存是否matrix[i][0]当行是否需要被清零
    #第一列和第一行本身用其他的状态位标识是否清零

        m, n = len(matrix), len(matrix[0])

        row0=any(matrix[0][j] == 0 for j in range(n)) #第0行是否有0元素
        col0=any(matrix[i][0] == 0 for i in range(m)) #第0列是否有0元素

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        #处理,如果这一个位置这一行或者列对应的标记为0，就把自己归零
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        
        if row0:
            for j in range(n):
                matrix[0][j] = 0
        if col0:
            for i in range(m):
                matrix[i][0] = 0
