#类似于不同路径
#dp[i][j]表示从起点(0,0)到达(i,j)的最小和
#要不是从上面(i-1,j)走下来，要不就是从左边(i,j-1)走过来，所以最小和等于这两者的最小值加上当前格子的值
#dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
#可以节省空间，直接在原数组上修改，最后返回右下角的值即可
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        
        # 1. 初始化第一列（只能从上面往下走）
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
            
        # 2. 初始化第一行（只能从左边往右走）
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
            
        # 3. 遍历其余格子，按照状态转移方程计算
        for i in range(1, m):
            for j in range(1, n):
                # 取左边和上面中的较小值，加上当前格子的值
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
                
        # 4. 返回右下角的值
        return grid[m - 1][n - 1]