# 287.寻找重复数
# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            count = sum(num <= mid for num in nums)
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left

class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        解法二：快慢指针（数组视为链表找环入口），弗洛伊德解法
        时间复杂度: O(N)
        空间复杂度: O(1)
        """
        slow, fast = 0, 0
        
        # 1. 第一阶段：寻找相遇点，判断是否有环
        while True:
            slow = nums[slow]           # 慢指针走一步
            fast = nums[nums[fast]]     # 快指针走两步
            if slow == fast:            # 必然在环内某处相遇
                break
                
        # 2. 第二阶段：寻找环的入口（即为重复的数字）
        slow = 0                        # 慢指针回到起点
        while slow != fast:             # 当没有再次相遇时
            slow = nums[slow]           # 这次两个指针每次都只走一步
            fast = nums[fast]
            
        return slow
