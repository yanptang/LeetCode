# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        1. 如果要在class的 def 写嵌套的def，记得使用self变成一个对象的所有方法都可以访问的变量
        2. 思路是，先从最小的元素开始，所以先左递到最小元素，回退一步就k--1，同时比较此时的val
        3. 按照中序的思路，先左递归-中间值比较，右递归
        4. 递归中止条件：叶子节点 not node，或者已经找到了 self.ANS NOT NONE
        '''
        self.k=k 
        self.ans=None

        def inorder(node):
            if not node or self.ans is not None: #如果已经命中也结束递归
                return 
            inorder(node.left) #左递
            self.k-=1 #退出来以后-1
            if self.k==0: #比较，如果命中，不再往右递，而是向上归 
                self.ans=node.val 
                return
            inorder(node.right)

        inorder(root)
        return self.ans