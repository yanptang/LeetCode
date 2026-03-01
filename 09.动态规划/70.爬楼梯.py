# 对于第n级台阶，可以从第n-1级台阶或第n-2级台阶跳上来
# 因此状态转移方程为：dp[n] = dp[n-1] + dp[n-2]
# 即任意一级台阶的跳法数等于前两级台阶的跳法数之和
class Solution:
    def climbStairs(self, n: int) -> int:
        # 处理边界情况，如果n为0或1，直接返回n
        if n <= 1:
            return n
        
        # 初始化dp数组，长度为n+1，dp[i]表示跳上第i级台阶的跳法数
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        # 从第2级台阶开始，按照状态转移方程计算每一级台阶的跳法数
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
        