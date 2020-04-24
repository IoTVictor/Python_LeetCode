'''
给定 1->2->3->4, 你应该返回 2->1->4->3.
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy

        while head and head.next:
            first_node = head
            second_node = head.next
            # 2、3顺序不能颠倒
            pre.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            # 法二：一次性赋值
            # pre.next, first_node.next, second_node.next = second_node, second_node.next, first_node
            # 后移
            pre = first_node
            head = first_node.next

        return dummy.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

S = Solution()
p = S.swapPairs(node1)
print(p.val)
print(p.next.val)
print(p.next.next.val)