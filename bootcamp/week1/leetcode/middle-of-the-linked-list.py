# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        number = 0
        dumy = head
        while dumy.next:
            number+=1
            dumy = dumy.next
        ans = number//2
        while number!=ans:
                head=head.next
                number-=1
        return head
        