class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #可变滑动窗口，借助set的不可重复性质来判断此元素是否出现过；如果出现就移动left直到删除
        left=0
        n=len(s)
        ans=0
        seen=set()
        for right ,ch in enumerate(s):

            while ch in seen:
                seen.remove(s[left])
                left+=1
            ans = max(right-left+1,ans)
            seen.add(s[right])

        return ans