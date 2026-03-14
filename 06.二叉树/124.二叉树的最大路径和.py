# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #路径既可以经过root，也可以不经过root
        #所以返回的时候，不能记录子树的和，而是选择其中最大的一条通路（即我们只能选一边
        #记录全局最大值
        self.maxSum = float('-inf')

        def dfs(node):
            if not node:return 0

            #递归调用
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            #向上计算
            curr_path=sum=node.val+left+right #叶子一开始left，right都为0
            self.maxSum = max(self.maxSum,curr_path)

            #返回上一层,返回的时候只能在左右各选一个大一些的
            return node.val+max(left,right)


        dfs(root)

        return self.maxSum

