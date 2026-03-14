# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #头节点可能会变
        dummy = ListNode(0, head)
        temp = dummy

        #每两个节点交换一次
        #当后面不足两个节点，就停
        #假设两个需要排序的节点的位置是n，n+1，那么排序前后就是n-1和n+2
        while temp.next and temp.next.next:
            #temp代表的是n-1
            node1=temp.next
            node2=node1.next

            #连头:先让n-1指向node2
            temp.next=node2

            #掉头：让node1连接n+2
            node1.next=node2.next

            #交换，node1和2交换顺序
            node2.next=node1

            #下一组，n-1的位置就是temp，即此时的node1
            temp=node1
        
        return dummy.next
            

            




        