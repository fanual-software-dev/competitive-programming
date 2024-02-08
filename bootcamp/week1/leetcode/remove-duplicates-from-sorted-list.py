# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dumy=ListNode(-101,head)
        slow=dumy
        while head:
            if head.val==slow.val:
                head=head.next
                slow.next=head
            else:
                head=head.next
                slow=slow.next
        return dumy.next