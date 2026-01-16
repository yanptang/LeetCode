# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #本质上是我们去最下面的节点，一层一层计算深度
        #先到最左的叶子节点，返回1
        #再由return不断返回，每一层就累加一个1
        def dfs(node):
            if not node:
                return 0 
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)

        return dfs(root)