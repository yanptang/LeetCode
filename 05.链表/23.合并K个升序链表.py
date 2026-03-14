# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #原始的链表已经是有序的链表
        #可以利用heap，最小堆来存要返回的内容
        #对于链表来说，每个链表的第一个都是队列里最小的，先全部进去，保证其中一个是所有node里最小的
        #出一个，就把刚出来的那个node的后面的加进来，这样保证了当前在heap里的三个一定有一个全局最小
        #每次链表后面加入当前的堆顶即可
        

        hp=[]
        dummy=ListNode(0)
        curr=dummy

        #初始化，k个最小值都进heap，进行第一轮排序
        #注意此刻的lists[i] 代表第i个链表的head
        for i in range(len(lists)):
            if lists[i]: #如果当前队伍有值
                #分别加入头节点（指向当前链表的第一个）的节点值，链表index，链表节点本身
                heapq.heappush(hp, (lists[i].val, i, lists[i]))

        while hp:
            val, i, node = heapq.heappop(hp)
            
            # 连接到结果链表
            curr.next = node
            curr = curr.next
            
            # 如果这个节点后面还有人，让那个人进堆
            if node.next:
                node = node.next
                heapq.heappush(hp, (node.val, i, node))

        return dummy.next