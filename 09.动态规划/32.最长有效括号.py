#正向记录，右括号多了截断归零
#反向记录同理，左括号多了截断归零
#每当相等，更新最大长度
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #双向计数法

        left,right,max_length=0,0,0

        #先考虑2种情况，正向扫描
        #1/扫完刚好相等，那么长度就是right/left的2倍
        #2/终于遇到右括号多了，直接把之前的串截断了，不能继续保留下去作为连续串

        
        for i in range(len(s)):
            if s[i]=='(':
                left+=1
            else:
                right+=1
            
            if left==right:
                max_length=max(max_length,2*left)
            
            #括号匹配有顺序，如果右括号在中间就多了，后面出现再多的左括号也没用，切断了前面的连续性
            elif right>left:
                left=right=0
        
        #但是字符串 ((())的情况，正向扫到最后不会出发任何left==right，也不触发条件2，所以要反向扫描一次
        left = right = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='(':
                left+=1
            else:
                right+=1
            
            if left==right:
                max_length=max(max_length,2*left)
            
            elif left>right:
                left=right=0

        return max_length

