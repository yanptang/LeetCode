class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #遍历循环求max
        #记录当前遇到得最低价，和最低价后面的最高价的价差
        #跟max对比

        max_profit=0
        min_price= float('inf')
        for p in prices:
            if p<min_price:
                min_price=p
            else:
                max_profit=max(max_profit,p-min_price)
        
        return max_profit

    