# 输入：coins = [1, 2, 5], amount = 11
# 先正着推一遍
# 发现如果amount=1，那么需要1个1元的硬币，dp[1]=1
# 如果amount=2，那么需要1个2元的硬币，dp[2]=1
# 如果amount=3，那么需要1个2元的硬币和1个1元的硬币，dp[3]=2

#对于当前要凑的金额 i，我们遍历每一个可以使用的硬币 coin
#如果当前金额 i 大于等于硬币 coin 的面值，那么我们就可以使用这个硬币

#本质上我门把需要的钱的数量，先转成钱的价值的组合，再去找到达这个金额的组合的数量

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0

        #对每一个金额
        #遍历计算每一个coins是否可以兑换，可以兑换就去寻找上一个最小的
        for i in range(1,amount+1):
            for coin in coins:
                if i>=coin:
                    dp[i]=min(dp[i],dp[i-coin]+1) #被使用了一次+1
        
        return dp[amount] if dp[amount]!=float('inf') else -1