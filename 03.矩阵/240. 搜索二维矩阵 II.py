from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #用第一列和第一行来定位
        #从右上角开始递减,直到逼近左下角
        

        if not matrix or not matrix[0]:
            return False
        
        m,n = len(matrix),len(matrix[0])
        i,j = 0,n-1

        while i <m and j>=0:
            if target==matrix[i][j]:
                return True
            elif target>matrix[i][j]:
                #肯定不可能在此行左边，向下移
                i+=1
            else:
                #在左边
                j-=1
        
        return False
