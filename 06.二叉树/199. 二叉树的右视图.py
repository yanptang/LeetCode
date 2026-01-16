# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        #BFS 下每一层的最后一个push出来
        ans=[]

        #创建deque
        queue=deque()
        queue.append(root)

        #BFS 正常层序遍历
        

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i==size-1: #只是在pop时加一个判断是否为本层最后一个
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right) 

        return ans
