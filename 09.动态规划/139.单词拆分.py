# 可以看成字符串版本的背包问题
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        #转换list->set 查询速度从n->1

        wordSet=set(wordDict)
        n=len(s)
        dp=[False]*(n+1)

        dp[0] = True

        #dp[i] 代表，从s[0：i] 是否可以被wordDict里的词组成
        for i in range(1,n+1): #遍历每个s[0：i]
            for j in range(i): #对每个s[0：i]再看拆分成s[0:j]和s[j:i]
                if dp[j] and s[j:i] in wordSet: 
                    dp[i]=True
        return dp[n]
    
#i代表s[0:i]，j代表s[0:j]
#if dp[j]---->>如果s[0:j]可以被wordDict里的词组成，并且
#and s[j:i] in wordSet--->>s[j:i]也在wordSet里，那么s[0:i]也可以被wordDict里的词组成