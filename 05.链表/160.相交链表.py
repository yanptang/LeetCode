# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #让他们互相走自己的路，里程就是a+b+c，会在节点相遇
        
        #新建两个head指针的复制
        pA=headA
        pB=headB

        #先让两个都走
        while pA!=pB:
            if pA:
                pA=pA.next #先走自己的，指向下一个A链表本身的下一个
            else:
                #当自己的走完了，移动到pB
                pA=headB

            if pB:
                pB=pB.next #先走自己的，指向下一个B链表本身的下一个
            else:
                #当自己的走完了，移动到pA
                pB=headA
        return pA
