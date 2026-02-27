#核心思想：每个位置的水位= MIN（左边最高，右边最高)- 当前柱子的高度
#双指针取巧的地方在于，不去遍历右边最高的，我只看对于当前位置，左边兜的住还是右边
#理论上对于一个位置来说，我如果左边更短，就只要知道左边目前谁最高就行了，因为右边一定接的住
#如果右边更多，我也只需要在意右边的最高
#所以有一个对于当前左右指针来说能依靠的左max，右max就好了
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <3:
            return 0 #如果只有两个柱子 兜不住水

        l,r = 0, n-1
        water = 0
        lmax,rmax = 0,0 #用来存储到了i点 左边和右边的最大高度

        while l<r:
            lmax=max(lmax,height[l]) #更新左侧最高值
            rmax=max(rmax,height[r]) #更新右侧最高值

            #这里操作左右是说当前算左指针存水还是右指针位置存水
            #逻辑是，如果左边更低，右边一定有可以兜住水的高度，所以只在意左边的最大
            #并且用左边的最大和当前比较就可以了
            if lmax<=rmax: #左侧更低
                water+= lmax-height[l]
                l+=1
            else:    #右侧更低
                water+= rmax-height[r]
                r-=1
        return water