'''
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, pre = head, None
        while cur:
            pNext = cur.next  # 先保存下一个节点，防止链表断开

            cur.next = pre  # 向前指
            pre = cur  # 向后移
            cur = pNext  # 向后移

        return pre  # 最后cur遍历到最后指向null，pre是反转后的头结点

        # 法二：一次性赋值
        # cur, pre = head, None
        # while cur:
        #     cur.next, pre, cur = pre, cur, cur.next  # 一次性赋值
        # return pre  # 最后cur遍历到最后指向null，pre是反转后的头结点

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

S = Solution()
p = S.reverseList(node1)
print(p.val)
print(p.next.val)
