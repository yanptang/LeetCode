# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #not root：空树，当然找不到 → 返回 None
        #root == p 或 root == q：命中了 p 或 q，本层就先把它向上汇报（返回该节点）
        #其实想要的是命中状态是和否
        if root == None or root == p  or root==q:
            return root 
        
        #后续遍历
        #核心思想是在左右子树里找p和q；
        #如果两边都有，本结点就是
        #如果只有一边有，就顺着节点向下找
        left= self.lowestCommonAncestor(root.left,  p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left!=None and right!=None: #如果左边和右边子树都返回了值，即命中，就返回本节点
            return root 
        
        #如果都在同一边，将会是left 和rigth其中一个是第一个命中p或者q的节点
        #也就是最近的一个公共节点
        return left or right

