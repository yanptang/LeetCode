# 300.最长递增子序列
# dp[i]表示以nums[i]结尾的最长递增子序列的长度
# 状态转移方程：dp[i] = max(dp[i], dp[j] + 1) 
# 即对于当前i，要是i比之前所有元素都大，那么就可以接在这些元素后面，否则还是保持原来的长度不变
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)

        dp=[1]*n #初始化一个n长度的状态序列

        #状态转移
        #从i开始，每次看前面是否都比自己小
        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1) #dp[j]表示当前i跟nums[0:j]的一个组合
        return max(dp)   