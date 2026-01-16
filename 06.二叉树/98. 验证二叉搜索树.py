# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #对任意节点，都有 left<root<right 
        #并且，对任意节点都有，小于右边的root，大于左边的root
        def dfs(node,low,high):
            if not node:
                return True
            
            val=node.val

            if not (low<val<high):
                return False

            return dfs(node.left,low,val) and dfs(node.right,val,high)


        return dfs(root,float('-inf'),float('inf'))


