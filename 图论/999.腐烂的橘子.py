from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #BFS
        #层序遍历
        #把每一分钟当成一层，记录每一分钟的状态

        #第一步，遍历整个网格，标记腐烂的橘子的坐标，记录新鲜橘子的剩余数->腐烂队列queue，fresh_count
        #第二部，BFS，每次队列的烂橘子，都会传染上下左右的好橘子
        #橘子状态变化的话，就加入腐烂队列，新鲜的橘子-1
        #直到新鲜橘子数=0
        #返回经过的层数

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_count = 0 

        #step1 遍历记录状态
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh_count+=1
        
        if fresh_count==0: return 0

        #STEP2:BFS
        minutes = 0
        while queue and fresh_count>0: #当还有烂橘子，且有新鲜橘子可以被腐烂
            minutes +=1
            
            for _ in range(len(queue)): #每一分钟都要把当前分钟的烂橘子处理完
                r,c = queue.popleft()
                for dr,dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc #每次烂橘子的污染对象
                    if 0<=nr<rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 # 传染
                        fresh_count -= 1 # 新鲜橘子少一个
                        queue.append((nr, nc)) # 新烂的橘子加入下一分钟的扩散队伍
        
        return minutes if fresh_count==0 else -1




