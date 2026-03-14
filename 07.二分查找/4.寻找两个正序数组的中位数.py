class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            # 辅助函数：寻找第 k 小的元素
            index1, index2 = 0, 0
            while True:
                # 特殊情况 1：nums1 已经排除光了
                # 就要返回另一个数组中的第k个小的元素
                if index1 == m:
                    return nums2[index2 + k - 1]
                # 特殊情况 2：nums2 已经排除光了
                if index2 == n:
                    return nums1[index1 + k - 1]
                # 特殊情况 3：k=1，直接找两个数组头部的最小值
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况：二分寻找
                # 比较两个数组的第 k/2 个元素，注意防止索引越界
                # 这个步骤就是在两个数组里逐步剔除比k/2小的元素
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                
                if nums1[newIndex1] <= nums2[newIndex2]:
                    # 排除 nums1 的一部分
                    # 这里排除的是比较的较小的部分的前面的值
                    k -= (newIndex1 - index1 + 1)
                    index1 = newIndex1 + 1
                else:
                    # 排除 nums2 的一部分
                    k -= (newIndex2 - index2 + 1)
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            # 奇数长度
            return getKthElement(totalLength // 2 + 1)
        else:
            # 偶数长度，取中间两个的平均值
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2.0