# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#翻转这棵二叉树；需要直接操作节点
#自己调用自己，一层一层的交换

'''
return None--None = 没有东西（空节点、空对象）
return 0 --有效数字0
return ""  # 空字符串
return []  # 空列表
'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        
        root.left,root.right = root.right,root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        