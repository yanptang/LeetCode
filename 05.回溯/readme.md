# 06 回溯
hello算法回溯章：https://www.hello-algo.com/chapter_backtracking/
回溯本质上是一个穷举法，提升效率的方法之一是剪枝
```Python
#回溯的框架代码
def backtrack(state: State, choices: list[choice], res: list[state]):
    """回溯算法框架"""
    # 判断是否为解
    if is_solution(state):
        # 记录解
        record_solution(state, res)
        # 不再继续搜索
        return
    # 遍历所有选择
    for choice in choices:
        # 剪枝：判断选择是否合法
        if is_valid(state, choice):
            # 尝试：做出选择，更新状态
            make_choice(state, choice)
            backtrack(state, choices, res)
            # 回退：撤销选择，恢复到之前的状态
            undo_choice(state, choice)
```
回溯经典问题
1. 搜索问题：这类问题的目标是找到满足特定条件的解决方案。（主要的）

- 全排列问题：给定一个集合，求出其所有可能的排列组合。
- 子集和问题：给定一个集合和一个目标和，找到集合中所有和为目标和的子集。
- 汉诺塔问题：给定三根柱子和一系列大小不同的圆盘，要求将所有圆盘从一根柱子移动到另一根柱子，每次只能移动一个圆盘，且不能将大圆盘放在小圆盘上。

2. 约束满足问题

- N皇后问题，在棋盘上的N皇后问题
- 数独问题
- 着色问题