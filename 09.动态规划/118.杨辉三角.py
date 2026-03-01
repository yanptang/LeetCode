# 杨辉三角
# dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #1. 初始化：如果numRows为0，返回空列表
        if numRows == 0:
            return []
        
        #2. 创建一个二维数组dp来存储杨辉三角的值，大小为numRows行，每行的列数等于行数（即第i行有i+1列）
        dp = []
        for i in range(numRows):
            dp.append([0] * (i + 1))

        #3. 填充杨辉三角的值：根据杨辉三角的性质，每行的第一个和最后一个元素都是1，其他元素根据状态转移方程计算
        for i in range(numRows):
            dp[i][0] = 1 # 每行的第一个元素是1
            dp[i][i] = 1 # 每行的最后一个元素也是1
        
        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] # 根据状态转移方程计算每个元素的值
        
        return dp