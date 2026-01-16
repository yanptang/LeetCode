# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #一层一层展开，先展开左子树
        #再展开右子数
        #对每一层操作：把右子树移到左子树的尾；再把node.RITGH->左子数
        #向上回溯这一过程
        
        def dfs(node):
            if not node :
                return None
            
            left_tail=dfs(node.left)
            right_tail=dfs(node.right)
            #关键逻辑
            if left_tail:
                left_tail.right = node.right #右子树移到左子树的尾
                node.right = node.left
                node.left =None
            #利用 Python 的“或”短路：谁先不是 None 就返回谁，恰好符合三种优先级
            return right_tail or left_tail or node 
            '''
            if right_tail is not None:
                return right_tail
            elif left_tail is not None:
                return left_tail
            else:
                return node
            '''

        dfs(root)