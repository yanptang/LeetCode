class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #用一个单调栈来存储index
        #其实就是一个暂存index的list，每次如果当前温度比栈顶元素低，就存进去
        #如果当前温度比栈顶元素高，说明当前温度就是栈顶元素/次栈顶元素的下一个高温天
        #那么间隔=当前的index-i --减 栈顶的index

        n = len(temperatures)
        ans = [0] * n
        st=[]

        for i in range(n):
            while st and temperatures[st[-1]]<temperatures[i]:
                ans[st[-1]]=i-st[-1]
                st.pop()
            st.append(i)
        return ans