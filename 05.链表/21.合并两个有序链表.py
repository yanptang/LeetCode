# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #像拉链一样把两个链表连起来，最后返回新链表的head
        dummy=ListNode(0) #新建一个head 作为返回的head
        curr=dummy   #每次会更新curr
        
        #先一个一个比较
        #小的先链接过去，然后移动到下一个结点继续比较
        while list1 and list2: #先比较同样的长度
            if list1.val<list2.val:#把小的结点连到新链表的后面
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            
            curr=curr.next #跳转到这次新链接的指针

        #一条走完以后，剩下的非空直接链接过去
        if list1 is not None:
            curr.next=list1
        else:
            curr.next=list2
        
        return dummy.next
          