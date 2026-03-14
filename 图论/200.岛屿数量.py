class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #当我扫描到一个1，把它相互连通的所有1都归类为0，计数器+1
        #再继续扫描

        #采用DFS，一直遍历到最底层，直到最后一次，返回到上一个有分叉的，继续遍历到底层
        #一般通过递归实现

        if not grid:
            return 0
        
        rows=len(grid)
        cols=len(grid[0])
        count=0

        def dfs(i,j):
            #递归遍历上下左右的1，直到所有的1都变成0
            #1.回退条件，遇到了矩阵边界 或者遇到了0
            if i< 0 or i>=rows or j<0 or j>=cols or grid[i][j]=='0':
                return
            
            #标记遇到的1为0
            grid[i][j]='0'

            #遍历上下左右
            dfs(i + 1, j) # 下
            dfs(i - 1, j) # 上
            dfs(i, j + 1) # 右
            dfs(i, j - 1) # 左

        #遍历网格
        for i in range (rows):
            for j in range(cols):
                if grid[i][j]=='1': #发现一个1，就要把上下左右所有的连通都变成0
                    count+=1
                    dfs(i,j)

        return count


        