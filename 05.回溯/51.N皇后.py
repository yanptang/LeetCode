class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #翻译题目，皇后不能处在同一行，同一列，同一对角线
        #即任意一点，如果有皇后，那么对应的行row，列col，对角线i+x，j+x都不能有第二个皇后

        #因此我们可以一行一行的放，并且放置以后，标记被占用的行，列，对角线，下次放置就不可以放了
        #对角线占用：任意一个点i,j放置以后，主对角线占用的坐标差是i-j，副对角线的坐标和是i+j


        res=[]
        # 初始化二维棋盘
        # [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
        board=[['.' for _ in range(n)] for _ in range(n)]

        #记录已经冲突的列和对角线
        cols = set()      # 列
        diag1 = set()     # 主对角线 (r - c)
        diag2 = set()     # 副对角线 (r + c) 

        def backtrack(row):
            #终止状态
            if row==n:
                solution =[]
                for r in board:
                    solution.append("".join(r))
                res.append(solution)
                return 

            #遍历每一行对应的每一种列情况
            for col in range(n):
                #检查冲突剪枝
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                #如果没有冲突
                #加入棋盘，标记占用
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                backtrack(row+1)

                #撤销加入
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        
        backtrack(0)

        return res
