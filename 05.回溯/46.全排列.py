#46.全排列
#https://leetcode.cn/problems/permutations/?envType=study-plan-v2&envId=top-100-liked
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        selected=[False]*n #因为可能出现重复，因此用一个 selected数组下表标记状态

        def backtrack(path):
            #1.回溯框架，判断解
            if len(path)==n:
                ans.append(path[:]) #一份拷贝,列表不能直接append，因为是用的地址
                return 
            
            #2.遍历所有可能性
            for i,x in enumerate(nums): #第一次运行的时候表示决定index=1的数组
            #3，通过if判断剪枝
                if not selected[i]:
                    #操作和更新
                    path.append(x)
                    selected[i]=True #selected的下标i表示对应原先nums的下标i被使用过了
                    #4.递归
                    backtrack(path) 
                    #5. 回退：当输出了一个答案的时候，回退操作
                    path.pop()
                    selected[i]=False

        backtrack([])
        return ans