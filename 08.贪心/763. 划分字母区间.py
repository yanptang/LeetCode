#一旦你在这个片段里写了一个字母（比如 'a'），那么全字符串里所有的 'a' 都必须被圈进这个片段

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
    
        #每遇到一个新字母，就看它最后一次出现在哪，把那个位置设为当前的“必须到达的边界”
        #如果遇到了更后的，就需要更新边界把他们包含进来
        #题目意思是，一旦一个字母出现在分段里，那就不能出现在别的分段里
        end_list=[]
        end=0
        start=0

        #先记录每个字符出现的最后的位置
        #{'a': 6, 'b': 5, 'c': 3, ...}
        last_position={char:i for i,char in enumerate(s)}

        #遍历字符串
        for i, char in enumerate(s):
            end=max(end, last_position[char])

            if end==i:
                end_list.append(end-start+1)
                start=end+1

        return end_list
        