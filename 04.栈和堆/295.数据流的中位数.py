#这个题目的难点是，放入的时候需要排序（方便找中位数，但是如果放一次排一次，时间复杂度很高
#所以我们的目标是，即快速访问，又能放进去后自动排序
#思路，任意一个排序好的列表，[1,2,3,4,5,6,7,8,9]，我们切成两半，左边存在max-heap，那么堆顶就是中间的左边元素
#同理，右边使用min-heap，堆顶就是右边的第一个元素
#返回的时候，只要返回他们的中间值就好了（其中一个，或者平均数
#但是每次还要判断左右吗？只要一开始的时候控制好左边<=右边多一个就好了，奇数的时候，就是左边堆顶，偶数，就是中间值
#存入的时候，跟堆顶元素值比较，存入以后自动排序
import heapq
class MedianFinder:

    def __init__(self):
        #初始化两个堆
        self.queLeft=[]
        self.queRight=[]
        
    
    def addNum(self, num: int) -> None:
        #存数字，python自带的heap是小堆顶，所以操作的时候对于left heap可以取反存
        #进来2，存-2
        heapq.heappush(self.queLeft, -num)

        #再把大顶堆的顶弹出来送进小顶堆
        heapq.heappush(self.queRight, -heapq.heappop(self.queLeft))

        #关键逻辑：数量平衡
        #右边多了，就从右边拿出一个还给左边
        #在这个倒手的过程中，自动完成了对进来的数字的大小分流
        if len(self.queLeft)<len(self.queRight):
            heapq.heappush(self.queLeft,-heapq.heappop(self.queRight))
        
    
    def findMedian(self) -> float:
        #如果是偶数
        #记住不需要pop，因为后面的元素要返回所有的值
        if len(self.queLeft)==len(self.queRight):
            return (-self.queLeft[0] + self.queRight[0]) / 2.0
        else:
            return -self.queLeft[0]


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()