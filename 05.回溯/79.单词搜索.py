    #solution条件 长度相等且word==
    #剪枝：不符合长度的搜索空间+不以这个字母开头的搜索空间
    #搜索策略：先找开头字母，比如A，然后前后左右的找，找到一层，再向下一层
    #每个回溯函数是完成一次前后左右的查找
    #避免使用同一个条件的格子，匹配上以后要立一个flag，并且如果不使用了要回退
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(i,j,k): #k表示当前需要搜索的字符串的第几个值
            #进来先判断是不是要找的元素
            #如果第一行向上找，最后一行向下找，导致数组会越界，就也不存在这样的解
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            
            #标记使用过
            tmp = board[i][j]
            board[i][j] = '#'

            #有解条件
            if k==len(word)-1:
                return True

            #下面完成四个方向的查找
            #任意一个方向命中即可，全部使用or条件
            #命中的那个方向会继续迭代dfs，直到返回有解条件True
            #如果最终匹配，res=True，否则为4个False
            res = (dfs(i + 1, j, k + 1) or
                    dfs(i - 1, j, k + 1) or
                    dfs(i, j + 1, k + 1) or
                    dfs(i, j - 1, k + 1))
            
            #回退，即如果当前匹配，但是往后找不到，就说明前面的序列都不行，一一回去回退
            board[i][j]=tmp

            return res

        
        
        #从第一个字母去遍历，先匹配首字母，如果完全不存在就跑完循环返回Flase
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):   # 找到了就直接返回 True
                    return True
        
        return False