#左右指针扫描的时候，要保证三元素的任意一个元素都不能重复
#因为找的时候，1个元素会把所有的组合情况都遍历了
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        n=len(nums)
        for i in range(n-2):
            if nums[i]>0: #当前的数是接下来的序列中最小的数 如果它大于0就不可能有组
                break 
            #重复元素不能用
            if i>0 and nums[i]==nums[i-1]:
                continue
            left,right = i+1,n-1
            while left<right:
                s = nums[i] + nums[left] + nums[right]
                if s==0:
                    ans.append([nums[i],nums[left],nums[right]])
                    #left/right有重复的也不能用
                    lv, rv = nums[left], nums[right]
                    while left < right and nums[left] == lv:
                        left += 1
                    while left < right and nums[right] == rv:
                        right -= 1
                elif s<0:
                    left+=1
                else:
                    right-=1
        return ans