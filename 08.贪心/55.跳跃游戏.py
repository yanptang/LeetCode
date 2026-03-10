class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #维护当前位置可以跳到的最长距离，查看是否超过下标
        max_reach=0
        n=len(nums)

        for i in range(n):
            #如果连当前的位置都到不了，就不能到最后了
            if i > max_reach:
                return False
            
            max_reach=max(max_reach,i+nums[i])

            if max_reach>=n-1: #记住边界条件
                return True
        
        return False