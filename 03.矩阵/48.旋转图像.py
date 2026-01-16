from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #先转置->行变成列，列变成行
        #每一行左右翻转，用左右指针，轮次交换

        n=len(matrix)

        #转置
        for i in range(n):
            #只需要对主对角线得右上方进行交换
            #否则会交换回去
            for j in range(i+1,n):
                #python特有得交换方式，不需要借助第三方
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            
        #左右翻转
        for i in range(n):
            l,r=0,n-1
            while l<r:
                matrix[i][l],matrix[i][r]=matrix[i][r],matrix[i][l]
                l+=1
                r-=1