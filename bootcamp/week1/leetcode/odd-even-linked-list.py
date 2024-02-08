# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur=head
        end=head.next
        count=1
        while head and head.next:
            count+=1
            temp=head.next
            prev=head
            head.next=head.next.next
            head=temp
            if head.next==None and count%2!=0:
                prev=head
        prev.next=end
        return cur