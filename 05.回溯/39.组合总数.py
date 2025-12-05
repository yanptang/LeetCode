
# 组合总数
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的数字可以无限制重复被选取。

#典型的回溯+剪枝问题
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def backtrack(target, start):
            if target == 0:
                ans.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                # 剪枝：当前 candidate 已经超过 target，后面更大，直接 break
                if candidates[i] > target:
                    break

                path.append(candidates[i])
                # 传递剩余 target，i 表示可重复选当前数
                backtrack(target - candidates[i], i)
                path.pop()

        backtrack(target, 0)
        return ans