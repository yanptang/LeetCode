class Solution:
    def jump(self, nums: List[int]) -> int:
        #保证可以到达 n - 1
        #每次跳跃，查看自己跳跃范围内，能贡献最大的跳跃范围的下标，跳过去
        #如果当前的下标已经到达自己跳跃的边界了，就不得不跳了

        #num[0]可以跳两步，而且自己是最后一个，必须要跳
        #可以选择3和1，所以选择3（通过遍历选择）


        max_reach,end,ans=0,0,0
        n=len(nums)

        for i in range(n-1):
            max_reach=max(max_reach,i+nums[i])

            #查看自己是要跳了，还是可以继续遍历(找最大值)
            #如果end超过max_reach的时候，这个循环本身结束就结束了
            if end==i:
                ans+=1
                end=max_reach #下次必须要跳的地方

                #优化
                if end>=n-1:
                    return ans
        return ans