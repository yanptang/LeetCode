# 437. 路径总和 III
# 给定一个二叉树的根结点 root，整数 targetSum ，求该二叉树中路径总和等于 targetSum 的路径数。
# 路径 不需要从根结点开始，也不需要在叶子结点结束，但路径方向必须是向下的（只能从父结点到子结点）。 
#https://leetcode.cn/problems/path-sum-iii/?envType=study-plan-v2&envId=top-100-liked

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        #如果规定了从根结点root开始，只需要执行一遍
        if not root:
            return 0
        
        def countFrom(node,target): #本函数是把第一层传入的node作为根结点回溯计算一遍以此为根的左右数的路径和
            if not node:
                return 0
            
            count=1 if node.val==target else 0
            count+=countFrom(node.left,target-node.val)
            count+=countFrom(node.right,target-node.val)
            return count
        
        return (countFrom(root,targetSum)
                #但是因为不规定必须从根结点开始，所以要把每个结点都当成一个根节点执行一遍最原始的函数
                +self.pathSum(root.left,targetSum) #记得加self，因为不是函数，而是对象的方法
                +self.pathSum(root.right,targetSum))