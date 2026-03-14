# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #先找到要删除的点，记录前后分别是谁，让前者指向后者即可
        #找删除节点：双指针，一个指针先出发k步，另一个紧随其后，等第一个到达终点，第二个
        #恰好跟终点的距离就是k

        #不直接用head，因为head可能会被删除，n=sz的情况
        #留下一个标记始终指向该链表的head
        dummy = ListNode(0, head)
        slow=fast=dummy

        #先让fast走n+1
        #因为我们希望slow停在n-1
        for i in range(n+1):
            fast=fast.next
        
        while fast:
            #当fast走到最后，slow刚好到n-1位置
            fast=fast.next
            slow=slow.next
        
        #删除节点
        #直接让slow指向next的next
        slow.next=slow.next.next

        return dummy.next




       