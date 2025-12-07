from typing import List
#74. 搜索二维矩阵
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        m = len(matrix)        # 行数
        n = len(matrix[0])     # 列数
        left=0
        right=m*n-1 #变成数字化序列的索引

        while left<=right:
            mid = (left+right)//2 #对应序列
            i= mid//n 
            j= mid%n
            if matrix[i][j]==target: 
                return True
            
            elif matrix[i][j]<target: #targer 在右侧
                left=mid+1
            
            else :
                right=mid-1
        
        return False
