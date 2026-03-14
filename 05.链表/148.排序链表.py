# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #sortlist会递归调用自身，切割为最小的节点，空或者单个，递归结束
        if head is None or head.next is None:
            return head
        
        #非单个点，用快慢指针切成两半
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #切割
        mid=slow.next #后半段的head
        slow.next=None

        #递归调用
        #比如传入[4,2]，得到left=[4],RIGHT=[2]
        left=self.sortList(head)
        right=self.sortList(mid)

        #比较合并
        return self.merge(left,right)
        

    def merge(self, left:ListNode, right:ListNode)-> ListNode:
        #新建一个head起点
        dummy=ListNode()
        tail=dummy #tail是合并后的链表的队尾，随着新增元素移动

        while left and right:
            #比较传入的head节点，即合并有序列表
            if left.val<right.val: #如果左边的人较小
                #较小的优先加入队尾
                tail.next=left
                #左队的人向前
                left=left.next

            else:
                #较小的优先加入队尾
                tail.next=right
                #右队的人向前
                right=right.next

            #把tail重定向为为下一个点，即队尾
            tail=tail.next

        #一队没有完事，一队完事了，剩下的直接连接
        if left is None:
            tail.next=right
        else:
            tail.next=left

        return dummy.next