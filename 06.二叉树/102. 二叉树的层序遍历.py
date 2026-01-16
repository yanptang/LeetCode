# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque #队列
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #经典 BFS（广度优先搜索）层序遍历
        #用队列来实现，访问一个根节点就把它放出来，并且把它的左右（一层）放进去
        #每次先把队列pop，再把节点的左右放进去待排

        if root==None:
            return []
        
        queue = deque() #创建一个双端空队列
        queue.append(root) 
        res=[]

        while queue:
            level=[]
            lens=len(queue) #本层有多少个要排的元素

            for i in range(lens):
                node= queue.popleft()
                level.append(node.val)


                if  node.left !=None:
                    queue.append(node.left)
                if  node.right !=None:
                    queue.append(node.right)
            res.append(level)
        return res
        