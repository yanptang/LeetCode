class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #通常的想法是遍历，找到一个删除一个，添加一个，但是下标会乱
        #所以要用双指针，一个用来记录现在删到哪里了，一个用来记录现在的队尾的编号

        delete = 0
        tail = len(nums)

        while delete<tail:
            if nums[delete]==0:
                nums.pop(delete)   #删除当前位置，但是delete此时就是下一个 不能继续操作了
                nums.append(0)
                tail-=1    #队尾
            else:
                delete+=1

