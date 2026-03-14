class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #切蛋糕逻辑
        #第一刀可以下在任何一处，但是要保证切下的左边是回文串
        #如果是的话，就继续往后切(往后任意一点都可以切)
        #如果不是，就直接放弃这一点下到
        #循环这个结构，直到切到末尾

        res=[]
        path=[] #当前记录的回文方案

        def backtrack(strat_index):
            #停止条件，如果切到最后一个字符
            if strat_index == len(s):
                res.append
                return
            
            #因为刀每一处都要下一次，所以for循环去切每一处
            #且确定了左边是回文以后，也要执行for，所以这个i是从每次调用的开始开始往后切
            for i in range(strat_index,len(s)):
                sub=s[strat_index,i+1]

                if sub==sub[::-1]: #如果是回文
                    path.append(sub)
                    backtrack(i+1) #继续往后切

            
    
        backtrack(0)    


        return res

        