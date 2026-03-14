"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #深拷贝，新链表中的结点都正确指向新链表的下一个节点，包括random指向关系
        #且random的指向也必须指向新链表中的节点，而非老节点
        #新旧两个链表在内存里应该是完全独立的，改动原链表，新链表不能有任何变化

        #原地拆分法
        #第一步，先原地插入新链表A -> A' -> B -> B' -> C -> C'
        curr=head
        while curr:
            #创建一个一样的节点，并且指向原先节点的下一个
            new_node=Node(curr.val,curr.next)
            #插入
            curr.next=new_node
            #移动
            curr=new_node.next 
        
        #第二步，复制随机指针A'.random=A.random.next
        curr = head
        while curr:
            if curr.random is not None:#如果radom存在
                curr.next.random=curr.random.next
            curr=curr.next.next

        #第三步，拆出来
        
        dummy=Node(0) #新节点的头和尾
        tail=dummy
        
        curr=head
        #A -> A' -> B -> B' -> C -> C'
        #第一轮，curr=A，next是A'判给tail
        #tail替换为A'进入下一论，curr是原链表的B，即新tail.next
        while curr:
            tail.next=curr.next
            tail=tail.next
            curr=tail.next
            
        return dummy.next

            