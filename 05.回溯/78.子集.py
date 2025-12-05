# 78. 子集
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
# https://leetcode.cn/problems/subsets/?envType=study-plan-v2&envId

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans=[]
        n=len(nums)

        def backtrack(start,path):
            ans.append(path[:])

             # 从 start 开始，尝试选择后面的元素
             # 因为不能选自己已经选过的元素 后续也不能重
            for i in range(start, n):
                path.append(nums[i])
                backtrack(i+1,path)
                #回退
                path.pop()


        backtrack(0,[])     

        return ans