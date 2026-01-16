# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #镜像相等的定义（对于任意node -p 一定可以找到一个 q 和它对应）
        #值相等：p.val == q.val
        #外侧相等：p.left ↔ q.right
        #内侧相等：p.right ↔ q.left

        #思路：DFS同时传入左和右节点，回溯搜索，同时对比以上条件


        def is_mirror(p,q):
            if not p and not q: #两节点都为空
                return True
            if not p or not q: #是否结构不一样了；即对应p点找不到q点
                return False
            if p.val != q.val: #是否结构一样，但是值不一样了
                return False 
            #再下一层检验，记得左边是left，右边应该为right
            #and 条件，任意一边不一样都不行
            return is_mirror(p.left, q.right) and is_mirror(p.right, q.left)

        return is_mirror(root.left,root.right) if root else True