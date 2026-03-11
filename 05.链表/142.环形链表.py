# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #弗洛伊德判圈算法 (Floyd's Cycle-Finding Algorithm)
        #先用快慢指针找相遇点
        #再把slow归零，找入口

        slow=fast=head

        
        while fast and fast.next is not None: #fast先走到了最后，没有环得结构
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                #找入口
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                
                return slow
        return None

