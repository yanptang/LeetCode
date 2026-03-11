#解法就是中心展开法，从一个字符往左右两边看，如果一样，就继续下一个，直到不一样的
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        #如果是1个或者空肯定就是回文串
        if n<2:
            return s 
        
        res = ""

        def expand(l,r):
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r] #注意：退出循环时，left 和 right 已经多走了一步
        
        for i in range(n):
            # 针对不同字符长度都看一遍，对比看哪个更长
            # 情况 1：回文长度是奇数，中心是一个字符
            s1=expand(i,i)
            # 情况 2：回文长度是偶数，中心是两个字符之间的空隙
            s2=expand(i,i+1)

            res=max(res,s1,s2,key=len)# 更新最长结果
        
        return res

        