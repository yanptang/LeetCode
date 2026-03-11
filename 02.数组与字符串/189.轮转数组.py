#189. 轮转数组
#三次翻转法
#想象数组是一根可以切断并重新连接的绳子。向右轮转 k 个位置，本质上就是把数组的末尾 k 个元素移动到开头,再翻转

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #先处理边界
        n=len(nums)
        k=k%n

        def rev(l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        
        rev(0,n-1)
        rev(0,k-1)
        rev(k,n-1)