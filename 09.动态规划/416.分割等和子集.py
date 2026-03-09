# 416.分割等和子集
# 两个子集和相等，说明每个子集的和为 sum(nums) // 2
# 0-1背包问题：每个数字只能用一次，问能不能凑出和为 sum(nums) // 2
# 记得从后往前推，避免重复计算
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #如果和是奇数，怎么也不能均分
        total = sum(nums)

        if total%2!=0:
            return False
        

        target=total//2

        # 2. dp[i] 表示能不能凑出和为 i
        dp = [False] * (target + 1)

        # 边界条件：凑出和为0永远是True（什么都不选即可）
        dp[0] = True

        # 3. 遍历物品（数组中的每个数字）
        for n in nums:
            #从target往回推，看能用组合数字组成什么
            #比如n=1，dp[1]==True
            #比如n=5，dp[5],dp[6]==True
            #比如n=11，dp[5],dp[11]==True
            for i in range(target,n-1,-1):
                dp[i]=dp[i] or dp[i-n] 
                #dp[i-n]表示当前的数字，可以跟之前记录过的数组成的数的结果
                #即我当前要这个数字，前提是之前的i-n也是可以凑成的
        return dp[target]