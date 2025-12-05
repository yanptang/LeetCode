# 17. 电话号码的组合
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 给出数字到字母的映射如下（与电话按键相同）。
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        #构建字典
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []
        path = []

        def backtrack(index):
            #solution条件
            if index==len(digits):
                ans.append("".join(path))
                return 
            
            # 当前数字对应的所有字母
            letters = phone[digits[index]]

            for ch in letters: #通过回溯实现多重循环->遍历空间
                path.append(ch)
                backtrack(index+1) #添加下一个号码
                path.pop()

        backtrack(0)
        return ans