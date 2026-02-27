#核心思想，双指针，两头扫描，移动短板，记录最大的面积，扫完以后返回最大值
#因为移动长的板子，不会使得高度增加，长板子->更长的板子，没用；长板子->短的，可能降低
# 面积计算=两个指针中间的距离*两个指针指向的短的那个的值
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        left = 0 #左指针
        right = len(height)-1 #右指针

        while left<right:
            distance=right-left
            short_way=min(height[left],height[right]) #这里注意比较的是值，要用下标去
            
            max_area=max(max_area,short_way*distance)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return max_area
        