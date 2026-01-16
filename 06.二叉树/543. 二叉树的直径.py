# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0#记得这里要用self；相当于创建一个属于本对象的全局变量

        def height(node: Optional[TreeNode]):
            if not node:
                return 0
            lh=height(node.left)
            rh=height(node.right)
            #ans是每一个节点自己最大左树+右数的数量
            self.ans=max(self.ans,lh+rh)
            #返回上一层的的时候，对于上一节点来说，只能选择一边高度
            #返回的是向上贡献的边数
            return 1+max(lh,rh)  
        
        height(root)
        return self.ans