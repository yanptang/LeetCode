class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #要找的是没有出现的，最小的正整数
        #先不管题目要求，通常的思路是，排序后，找到数组里最小的正整数-1
        #因为不能用额外的空间，所以我们采用原地交换的方式，尽量实现排序的过程
        #可以考虑使用index坐标作为参考点
        #让每个正整数n，都放在index为n-1的index，比如数字 1 应该住在 nums[0]
        #排序以后，发现的第一个坐标x没有对应的x+1数就是缺失数
        n=len(nums)
        for i in range(n):
            #正整数
            #且在排序区间内（防止溢出
            #是否在自己该有的位置上（如果已经有重复元素，就不需要换了，比如3应该在num[2]，如果相等表示已经有一个正确的3在上面了
            while nums[i]>0 and nums[i]<=n and nums[i]!=nums[nums[i] - 1] :
                target = nums[i] - 1
                nums[i], nums[target] = nums[target], nums[i]
        
        #找第一个不在自己位置的数据
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        
        #恰好顺序填充[1,2,3,4]，那么返回5
        return n+1
        
