#思路：先算一遍左边的累乘，再算一遍右边的累乘，每个数最后的结果=对应位置左边累乘*右边累乘
#其实就是双指针思路
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        ans=[1]*n  #用来存答案

        #计算前缀积
        #前缀积：ans[i] = nums[0..i-1] 的乘积
        prefix=1
        for i in range(n):
            ans[i]=prefix   #i=0的时候，左边乘积为1
            prefix *= nums[i]
        
        suffix=1
        # 后缀积：用一个变量从右往左累乘，再乘到 ans[i] 上
        for i in range(n-1,-1,-1):
            ans[i] *= suffix  #i=n-1的时候，右边乘积为1，所以×自己
            suffix *= nums[i] #更新，给下一个用
            
        return ans
