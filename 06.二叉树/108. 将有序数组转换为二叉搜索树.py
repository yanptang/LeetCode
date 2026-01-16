# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #什么是二叉搜索树（BST）
        #左子树所有节点的值 < 当前节点值；右子树所有节点的值 > 当前节点值
        #平衡 = 任意两个子树的高度差不能太大

        #疯狂二分法
        if not nums: return None
        m = len(nums)//2
        root = TreeNode(nums[m]) #构建一个节点
        root.left  = self.sortedArrayToBST(nums[:m])
        root.right = self.sortedArrayToBST(nums[m+1:])

        return root

        