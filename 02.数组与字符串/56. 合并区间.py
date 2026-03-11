
#56. 合并区间
#要点是先排序，再找重叠区间，最后合并区间
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #先排序
        intervals.sort(key=lambda x:x[0])
        
        #用not list来查看是否为空列表，是的话返回TRUE
        result=[]
        for every in intervals:
            
            if not result:
                result.append(every)
            
            #如果发生重叠，就将当前区间的末尾替换为合并区间的末尾
            elif result[-1][1]>=every[0]:
                result[-1][1]=max(result[-1][1], every[1])
            
            #不发生重叠，直接导入
            else:
                result.append(every)

        return result