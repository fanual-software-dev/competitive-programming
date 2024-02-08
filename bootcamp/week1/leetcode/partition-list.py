# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        less=0
        great=0
        curr=ListNode()
        dumy=ListNode()
        big=ListNode(-101)
        small=ListNode(-101)
        while head:
            if head.val>=x:
                if great==0:
                    curr=head
                    big=curr
                    great=1
                else:
                    curr.next=head
                    curr=curr.next
            else:
                if less==0:
                    dumy=head
                    small=dumy
                    less=1
                else:
                    dumy.next=head
                    dumy=dumy.next
            head1=head.next
            head.next=None
            head=head1
        if big.val!=-101:
            dumy.next=big
        
        return small if small.val!=-101 else big
        