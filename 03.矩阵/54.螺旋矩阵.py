from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #如果矩阵不存在，或者矩阵存在但没有任何列，直接返回空结果
        if not matrix or not matrix[0]:
            return []
        
        m,n = len(matrix),len(matrix[0])
        top,bottom = 0,m-1
        left,right = 0,n-1

        res=[]

        while top<=bottom and left<=right:
            #从左到右，列变化，top不变化
            for j in range(left,right+1):
                res.append(matrix[top][j])
            top+=1
            
            #从上到下，行变化，列不变化
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1
            
            #从右到左
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            
            #从下到上
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        
        return res
            