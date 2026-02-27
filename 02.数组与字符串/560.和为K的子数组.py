from collections import defaultdict
#核心思想：当我们走到位置 i 时，只要知道之前出现过多少次前缀和等于 pre[i] - k
#任何一个子数组 nums[j...i] 的和都可以表示为前缀和的差值
#Sum(j, i) = pre[i] - pre[j-1]
#令以上等于k，就可以得到 pre[j-1] = pre[i] - k
#对于例子[1,2,-2,3,4,5],K=12来说，前面的便利会存储cnt[1]=2，等计算到最后，发现pre-k=1，就获取cnt[1]=2加入ans


#三个关键参数
#cnt-字典，记录前缀和数字出现的次数
#pre-k，字典的索引，用来获取某个前缀和出现的次数，也即对应的解个数
#pre-计算前缀和
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #创建一个字典，如果访问不存在的key，自动返回0,普通字典会返回错误信息
        cnt = defaultdict(int) 
        cnt[0]=1

        pre=0 #记录前缀和
        ans=0

        for x in nums:
            pre+=x #计算前缀和
            ans+=cnt[pre-k] #把符合条件的多少次前缀和等于 pre[i] - k
            cnt[pre]+=1 #记录前缀和出现的次数
        
        return ans 