# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        mid = self.getMid(head)

        left = head
        right = mid.next

        mid.next = None  #

        return self.merge(self.sortList(left), self.sortList(right))  # 合并

    def merge(self, p1, p2):
        dummy = ListNode(None)
        cur = dummy
        while p1 and p2:
            if p1.val < p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next

        if p1 != None:  # p1链有剩余
            cur.next = p1
        elif p2 != None:  # p2链有剩余
            cur.next = p2

        return dummy.next

    def getMid(self, node):  # 获取链表的中间点
        if not node:
            return node
        fast = node
        slow = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow