class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #dp[i][j]= text1[0...i-1] 和 text2[0...j-1] 的最长公共子序列的长度
        #转移方程：两两对比，d[1][1]对比的就是text1[0] and text2[0]的最长序列
        #对比的时候，如果当前符号相等，那么就公共长度+1
        #如果不相等，就需要扔掉其中一个，去找下一个相等的，这个时候可以选择保留两者大一点的

        m,n=len(text1),len(text2)
        #字符串要考虑空串，dp[0]就是表示空
        dp=[[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        return dp[m][n]
        