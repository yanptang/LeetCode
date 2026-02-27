class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        len1,len2=len(s),len(p)
        if len1<len2:
            return []
        
        need=Counter(p)
        ans=[]

        left=0
        window=Counter(s[:len2])
        if window==need:
            ans.append(left)
        
        for right in range(len2,len1):
            #更新window信息
            window[s[right]]+=1
            window[s[left]] -=1

            if window[s[left]]==0:
                del window[s[left]]
            
            left+=1 #做完更新以后，更新left的index指向新的窗口
            if window == need:
                ans.append(left) 
            
        return ans