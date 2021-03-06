# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        node = result
        
        while l1 is not None or l2 is not None:
            if l1 is None:
                node.next =  l2
                node = node.next
                l2 = l2.next
            elif l2 is None:
                node.next =  l1
                node = node.next
                l1 = l1.next
            elif l1.val <= l2.val:
                node.next =  l1
                node = node.next
                l1 = l1.next
            elif l1.val > l2.val:
                node.next =  l2
                node = node.next
                l2 = l2.next

        return result.next