# 25. K 个一组翻转链表
#重点是，先找K个数，切断，放到翻转函数中，翻转函数提供翻转后的头，接在上一段的尾巴pre
#一开始的start这个时候变成了尾巴，指向还没有翻转的下一段的头nxt_group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head

        #dummy不能移动，用pre作为起始
        #因为pre要在排序中依次迭代，所以计数用tail
        pre=dummy
        #1.查看本组数据是否满足K

        while head:
            #1.如果一组数不够K，就不需要执行反转，那么请将最后剩余的节点保持原有顺序
            tail=pre
            for i in range(k):
                tail=tail.next
                if not tail:
                    return dummy.next
            #记录下一组的开头
            nxt_group=tail.next

            #2.先对于选出一组k的数进行翻转
            #先切断本组，方便做翻转的时候while状态切断
            tail.next=None
            start=pre.next
            new_head=self.reverse(start) #反转后的组的起点

            #3.合并两个组
            #翻转出来的组，返回的值变成了开头，要去衔接上一段的尾巴pre
            pre.next=new_head

            #star变成了开头，要去接还没有翻转的头
            start.next=nxt_group
            
            # 4. 更新状态
            pre=start
            head=nxt_group
            
        return dummy.next

    def reverse(self, curr: ListNode) -> ListNode:
        #先记录下一个节点，防止回头找不到
        prev = None
        while curr:
            next_node=curr.next
            #把传进来的curr反转
            curr.next=prev
            #向前迭代
            prev=curr
            curr=next_node
        return prev #返回本段的最后一个节点，也就是本组的尾巴,比如进入1->2>3,返回的是1<-2<-3中的3