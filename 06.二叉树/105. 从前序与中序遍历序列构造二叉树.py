# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder==[]:
            return None

        #前序列表用来确定根节点
        #中序列表用来确定左右子树

        #1. 中序每次都要查index，用字典存储，降低时间复杂度
        pos={}
        for i,v  in enumerate(inorder):
            pos[v]=i   #index是value，val是key

        #创建全局变量preindex，这个数据每执行一次迭代就更新一次，因为指向的是当前的root
        self.preindex=0
        n=len(preorder)

        def build(l,r):
            if l>r: #表示传入的节点左右子树没有区间了，自己就是叶节点
                return None
            
            root_val=preorder[self.preindex]
            self.preindex+=1
            root = TreeNode(root_val)

            i=pos[root_val]
            root.left=build(l,i-1) #传入左子树
            root.right=build(i+1,r) #传入右子树
            
            return root 
        
        return build(0,n-1)

        

        