# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #找中点 → 反转后半链表 → 两边比较
        #1.用快慢指针找到中点
        #快指针每次走2步，慢指针每次走1步，快指针到终点时，慢指针正好在中间
        slow,fast= head,head
        while fast and fast.next: #防止next next越界
            slow=slow.next
            fast=fast.next.next
            

        #2/反转链表->新链表以prev开头
        prev = None #prev存要做为下一个节点的node
        cur = slow
        while cur:
            next_node=cur.next
            cur.next = prev 
            prev = cur  #prev最后会变成新链表的头
            cur = next_node #cur会变成None 因为是在原链表里

        #3/逐个比较
        left=head
        right=prev 
        while right:
            if left.val != right.val:
                return False
            left  = left.next 
            right = right.next
        return True