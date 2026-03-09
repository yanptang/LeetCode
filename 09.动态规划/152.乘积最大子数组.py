# 152.乘积最大子数组
# 子数组：数组中的元素在原数组中是连续的。

#状态转移方程：
#对于任意一个元素nums[i]，要么：
# 1.它自己是一个新的子数组：nums[i]
# 2.它与前面最大的子数组相乘，形成一个新的子数组：max_dp[i-1] * nums[i]
# 3.它与前面最小的子数组相乘，形成一个新的子数组：min_dp[i-1] * nums[i]
#因此，状态转移方程为：
# dp[i] = max(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])
# 同时更新最小值：
# min_dp[i] = min(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #关键在于同时维护当前最大值和最小值
        #因为如果遇到负数，之前的最小值可以负负得正

        n=len(nums)
        max_dp=[0]*n
        min_dp=[0]*n
        
        max_dp[0]=nums[0]
        min_dp[0]=nums[0]

        for i in range(1,n):
            cur_num=nums[i]
            max_dp[i] = max(cur_num,max_dp[i-1]*cur_num,min_dp[i-1]*cur_num)
            min_dp[i] = min(cur_num,max_dp[i-1]*cur_num,min_dp[i-1]*cur_num)

        return max(max_dp)
