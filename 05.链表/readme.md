用python实现链表

# 链表节点的标准定义
class ListNode:
    def __init__(self, x):
        self.val = x      # 节点存的值
        self.next = None  # 指向下一个节点的指针（引用）


# 创建三个孤立的节点
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# 像串手串一样把它们连起来
node1.next = node2
node2.next = node3

# 现在我们有了一个链表：1 -> 2 -> 3
# 遍历链表并打印每个节点的值
current = node1  # 从链表的头节点开始
while current is not None:
    print(current.val)  # 打印当前节点的值
    current = current.next  # 移动到下一个节点
# 输出：
# 1
# 2
# 3

# 比较节点
if node1.val == node2.val:
    print("节点1和节点2的值相等")
else:
    print("节点1和节点2的值不相等")

#比较是否是同一个节点
if node1 is node2:
    print("节点1和节点2是同一个节点")
else:
    print("节点1和节点2不是同一个节点")


#哑节点的使用，无论 head 怎么变，dummy.next 永远能帮你找到链表的起点
dummy = ListNode(0)  # 创建一个哑节点，值为0
dummy.next = node1  # 哑节点指向链表的头节点    