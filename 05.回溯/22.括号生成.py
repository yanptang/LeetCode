#22.括号生成
#数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#示例 1：
#输入：n = 3
#输出：["((()))","(()())","(())()","()(())","()()()"]


#此题关键在于判断有效括号组合，#有效括号组合的特点是：在任意位置，左括号的数量都不少于右括号的数量，且最终左右括号数量相等。
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #solution条件：左右括号相等
        #剪枝条件：右边括号超过左边括号->left和right标志来记录现在几个括号
        #操作：还能放左就放左，不能放就放右；相等就停止
        #激活：放入一个激活一个
        
        res=[]
        def backtrack(path,left,right):
            if left ==n and right==n:
                res.append(path)
                return 

            #剪枝和操作在一起
            if left<n:
                backtrack(path+"(",left+1,right)
            
            if left>right:
                backtrack(path + ")", left, right + 1)


        backtrack("",0,0)
        return res
        