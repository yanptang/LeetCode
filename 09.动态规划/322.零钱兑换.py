# 输入：coins = [1, 2, 5], amount = 11
# 先正着推一遍
# 发现如果amount=1，那么需要1个1元的硬币，dp[1]=1
# 如果amount=2，那么需要1个2元的硬币，dp[2]=1
# 如果amount=3，那么需要1个2元的硬币和1个1元的硬币，dp[3]=2

#对于当前要凑的金额 i，我们遍历每一个可以使用的硬币 coin
#如果当前金额 i 大于等于硬币 coin 的面值，那么我们就可以使用这个硬币

#本质上我门把需要的钱的数量，先转成钱的价值的组合，再去找到达这个金额的组合的数量

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        零钱兑换 - 动态规划 (完全背包问题)
        
        时间复杂度: O(amount * n)，其中 n 是硬币的种类数
        空间复杂度: O(amount)
        """
        # dp[i] 表示凑成金额 i 所需的最少硬币数
        # 初始值为 float('inf')，方便后续求 min
        dp = [float('inf')] * (amount + 1)
        
        # 边界条件：凑金额0需要0个硬币
        dp[0] = 0
        
        # 遍历从 1 到 amount 的每一种金额
        for i in range(1, amount + 1):
            # 遍历每一种硬币
            for coin in coins:
                # 只有当硬币面额 <= 当前金额时，才能使用这个硬币
                if coin <= i:
                    # 转移方程：选择用这枚硬币，个数就是 dp[i-coin] + 1
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        # 如果 dp[amount] 还是无穷大，说明没有组合能凑出该金额，返回-1
        return dp[amount] if dp[amount] != float('inf') else -1


# 测试
if __name__ == "__main__":
    solution = Solution()
    print(solution.coinChange([1, 2, 5], 11))  # 输出: 3 (5+5+1)
    print(solution.coinChange([2], 3))         # 输出: -1
    print(solution.coinChange([1], 0))         # 输出: 0