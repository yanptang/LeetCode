#方法，常规解法，复杂度为(nlogn)
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if nums==[]:
#             return 0
#         nums.sort()
#         count=0
#         max_count=0
#         for i in range(0,len(nums)-1):
#             if nums[i+1]==nums[i]+1:
#                 count+=1
#                 max_count=max(count,max_count)
#             elif nums[i+1]==nums[i]:
#                 continue
#             else:
#                 count=0
#         return max_count+1

#哈希集合 set 做“只从起点扩展”的做法
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums) #不用set就会时间超限
        best = 0
        for x in s:
            if x - 1 not in s:      # 只从“序列起点”开始数
                y = x
                while y in s:
                    y += 1
                best = max(best, y - x)
        return best
