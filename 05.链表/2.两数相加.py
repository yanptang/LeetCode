# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #从头开始计算
        #中间主要是处理进位问题->carry 存，
        #长短不一的问题，补0
        #最后的进位

        dummy =ListNode(0)
        curr=dummy

        #存储进位信息
        carry=0

        #只要 l1 有数，或者 l2 有数,还有进位没加完，就继续循环
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0 #不对的位数用0 补齐
            v2=l2.val if l2 else 0

            #分位求和
            total = v1+v2+carry
            carry = total//10  #到下一位就是+跟10除取整
            val=total%10 #剩下的个位数

            #新节点
            curr.next=ListNode(val)
            curr=curr.next

            #进行下一位加法
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        
        return dummy.next



        