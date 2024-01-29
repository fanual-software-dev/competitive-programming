# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        count=1
        dumy=ListNode(-501,head)
        temp=dumy
        while head:
            if count==left:
                temp1=head
                prev=None
                while count<=right:
                    temp3=head
                    temp2=head.next
                    head.next=prev
                    prev=head
                    head=temp2
                    count+=1
                else:
                    temp.next=temp3
                    temp1.next=head
                    break
            else:
                count+=1
                temp.next=head
                temp=temp.next
                head=head.next
        return dumy.next
        