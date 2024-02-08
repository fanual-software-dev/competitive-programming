# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp=head
        count=0
        while head:
            count+=1
            head=head.next
        len=1
        temp2=temp
        if count==1 or count==n:
            return temp2.next
        while n!=count-len:
            temp=temp.next
            len+=1
        temp.next=temp.next.next
        return temp2