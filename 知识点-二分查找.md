参考资料：https://www.hello-algo.com/chapter_searching/binary_search/

二分的核心思想：
   排序，从中间开始遍历，每次根据判断大小来决定寻找方向

应用场景：
    查找，尤其是有序数组对于特定元素的查找
    插入，不改变顺序的情况下的元素插入
    查找元素的边界，例如重复元素中第一次出现的时候，或者什么时候结束（右边界

实现：
    1.通过双指针实现，每次计算 （i+j）/2，其中i和j为当前搜索空间的首尾，记得包含i，j
    1. 因为i，j都是int，为了避免i+j超过int的取值范围，因此也通常表述为 m = i + (j - i) / 2（python可以不考虑)


查找插入点的通用做法
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #使用二分查找
        left, right = 0, len(nums) - 1
        #注意这里的等于，就是当元素不存在的时候，收敛到一个比元素小的值上了,只用于不重复的数组，否则会陷入相等的循环
        while left<=right:       
            mid = (left + right) // 2  # 计算中点索引 m
            if nums[mid] == target: 
                return mid
            elif nums[mid] < target: #target在右侧，left移动
                left = mid + 1
            else:
                right = mid - 1

        return left #如果元素大于左边界，就会调入left = mid + 1；如果小于，就会应该放在左边left原先的位置
```


寻找边界的通用做法
```python
def lower_bound(nums, x): ##lower_bound标准写法，返回第一个满足 nums[i] >= x 的下标
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < x:
                    left = mid + 1  # m 及其左边都不可能 >= x
                else:
                    right = mid     # m 可能是答案，收缩右边界到 m
            return left
```