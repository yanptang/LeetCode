# 153. 寻找旋转排序数组中的最小值
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 请找出其中最小的元素。
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1

        if nums[left]<nums[right]: #已经恰好换成了原始数组
            return nums[left]
        else:
            #否则需要继续去找
            #特点，右半段是递增的，如果一个mid跟最右比较，要更大，说明就是 7 0 1 2 3，其中mid是7的情况
            #否则就是最小值在左边
            while left<right:
                mid=(left+right)//2
                if nums[mid]>nums[right]: #说明此时mid在旋转侧的元素里，最小值一定在mid的右边
                    left=mid+1
                else:                     #如果mid小于或者等于right，说明mid落在了右半段
                    right=mid
        return nums[left]