class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #本来是递增的数组，在旋转后，从k处开始，左右分别保持递增，但是nums[k]和nums[k+1]却一定有nums[k]>nums[k+1]
        #在[0,k],[k+1,n-1]中间可以继续二分；同时有num[k]是左边大的，num[n-1]是右边最大的
        #对于每一个mid，要判断左右哪边是有序的

        #利用特性，每次要先用num[left],num[mid]判断哪一段有序，再看target是否再有序的这一段（因为是递增的
        #如果不是就去另一边

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
             # 左半段有序
            if nums[left] <= nums[mid]:
                # target 落在左半段
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # 右半段有序
            else:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1

        return -1 