# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 141.环形链表
# 快慢指针：如果链表中存在环，则快慢指针最终会相遇；如果链表中不存在环，则快指针会先到达链表末尾。
# 即跑步套圈，虽然可能第一圈没追上，但是循环下去，一定会套圈追上

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=fast=head  #指向链表head
        
        #fast != None   AND   fast.next != None
        while fast and fast.next: #如果没有环的存在，fast会指向末尾；解除while循环
            slow=slow.next #每次slow移动一步
            fast=fast.next.next #每次fast移动两步

            if slow==fast: #当她们相遇的时候；两个引用指向同一个 Node 对象
                return True
        return False 