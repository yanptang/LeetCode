class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs==[""]:
            return [[""]]
        #创建一个就算没key也不报错的列表，如果不存在就自动创建此key
        from collections import defaultdict 
        mp=defaultdict(list)

        for s in strs:
            key=''.join(sorted(s)) #对字符串做排序，作为key  sorted是内置排序函数，返回列表
            mp[key].append(s)

        return list(mp.values())