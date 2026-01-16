from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            #使用异或的特性，相同的数字异或结果为0，0和任意数字的异或为本身
            #底层是二进制去异或的，不需要管中间变量
            #两个相同元素先后异或，一定抵消为0，只剩下一个单独元素x和其他所有的0异或，返回本身
            ans = ans^x 
        return ans 