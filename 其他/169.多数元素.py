#用Counter；再用.most_common方法
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         from collections import Counter
#         result=Counter(nums)
#         element, freq = result.most_common(1)[0]
#         return element

# #方法二：排序;多数元素一定占中间位置
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[len(nums)//2]


#Boyer-Moore 投票算法
#如果一个数出现次数超过 n/2，那么它比其他所有数加起来还多
#所以当票数为0的时候，替换候选人，出现一样的就+1，否则减1，如果为0，就换人
#核心是，出现一个多数元素，就抵消一个非多数元素，最后一定是多数元素多一些
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=None
        count=0

        for n in nums:
            if count==0:
                candidate=n
            if candidate==n:
                count+=1
            else:
                count-=1
        return candidate