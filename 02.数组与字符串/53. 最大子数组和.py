class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane‘s算法
        #从第一个数开始加，遇到下一个数"
        #如果是负数，那它只会拖累当前元素，所以直接从当前元素重新开一个子数组更优；如果是正数，就把它接上

        dp=nums[0]
        ans=nums[0]

        for n in nums[1:]:
            dp=max(n,dp+n)  #要不加上，要不重开
            ans=max(ans,dp)

        return ans