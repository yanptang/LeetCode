# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #对于任意一个node，要记住当前，用于下一个来找自己
        #也要记住本来的next是谁，用于继续往后迭代

        curr=head
        pre=None

        while curr:
            #记录原本的下一个是谁
            next_node=curr.next

            #调转
            curr.next=pre

            #当前的curr作为下一个的指向
            pre=curr

            #回到本来的next上
            curr=next_node
        
        return pre #记得返回的是pre，它此时停留在原先链表的最后一个，原先链表已经反转了，也就的需要的

