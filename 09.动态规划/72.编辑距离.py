#状态定义
# dp[i][j]表示将word1[0:i]转换成word2[0:j]的最小编辑距离
#状态转移方程
# dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + cost)
# 其中cost = 0 if word1[i-1] == word2[j-1] else 1
# 解释：要将word1[0:i]转换成word2[0:j]，可以考虑三种操作：
# 1. 删除word1[i-1]：dp[i-1][j] + 1
# 2. 插入word2[j-1]：dp[i][j-1] + 1
# 3. 替换word1[i-1]为word2[j-1]：dp[i-1][j-1] + cost


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # 创建 m+1 行 n+1 列的 dp 数组
        # 用dp[0][0]引入空字符串的概念
        #这里的dp[i][j]表示把word1[0,i-1]-->word2[0,j-1]的最小步数
        dp = [[0] * (n + 1) for _ in range(m + 1)]


        #边界条件是任意为空，要不一直插入，要不一直删除
        #word1 为空，一直插入
        for j in range(1,n+1):
            dp[0][j]=j

        #word2为空，一直删除
        for i in range(1,m+1):
            dp[i][0]=i


        for i in range(1,m+1):
            for j in range(1,n+1):
                # 如果当前字符相同，不需要增加额外操作
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j]=min(
                        dp[i][j - 1],    # 插入操作,把word[0:i]==word[0,j]
                        dp[i - 1][j],    # 删除操作,把word1[0:i-1]变成word2[0:j]
                        dp[i - 1][j - 1] # 替换操作,把word1[0:i-1]变成word2[0:j-1]
                    )+1
        return dp[m][n]