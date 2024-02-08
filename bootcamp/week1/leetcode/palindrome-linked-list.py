# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        coll=[]
        while head:
            coll.append(str(head.val))
            head=head.next
        s="".join(coll)
        return s==s[::-1]