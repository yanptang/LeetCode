# 状态定义 dp[i]=打家劫舍到第i家能偷窃的最大金额
# 状态转移方程 dp[i]=max(dp[i-2]+nums[i],dp[i-1])
# 对于任意一家，需要决定偷窃还是不偷窃，如果偷窃，那么就不能偷窃前一家，所以金额为dp[i-2]+nums[i]
# 如果不偷窃，那么金额为dp[i-1]

#边界条件 dp[0]=nums[0] dp[1]=max(nums[0],nums[1])
class Solution:
    def rob(self, nums: List[int]) -> int:

        n=len(nums)
        if n==1:
            return nums[0]
        
        dp=[0]*n
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])

        #对于任意一家，需要决定偷窃还是不偷窃，如果偷窃，那么就不能偷窃前一家，所以金额为dp[i-2]+nums[i]
        for i in range(2,n):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        
        return dp[n-1] 