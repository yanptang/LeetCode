from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #就是不使用sort排序的升序排序
        #维护三个指针，low，high，mid
        #分别用来记住，0存放得位置，2存放得位置，当前扫描的位置，也就是1对应的位置

        low,mid,high=0,0,len(nums)-1

        while mid<=high: #记住这个等于号
            if nums[mid]==0:
                nums[low],nums[mid] =nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            
            else:
                nums[high],nums[mid] =nums[mid],nums[high]
                high-=1