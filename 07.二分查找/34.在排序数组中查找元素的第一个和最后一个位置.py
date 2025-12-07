#34. 在排序数组中查找元素的第一个和最后一个位置
#把target-0.5和target+0.5分别作为lower_bound的参数进行查找
#变成一个寻找第一个大于等于x的下标的问题
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def lower_bound(nums, x): ##lower_bound标准写法，返回第一个满足 nums[i] >= x 的下标
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < x:
                    left = mid + 1  # m 及其左边都不可能 >= x
                else:
                    right = mid     # m 可能是答案，收缩右边界到 m
            return left
        
        left_index=lower_bound(nums,target-0.5)
        right_index=lower_bound(nums,target+0.5)-1
        if left_index<=right_index:
            return [left_index,right_index]
        else:
            return [-1,-1]