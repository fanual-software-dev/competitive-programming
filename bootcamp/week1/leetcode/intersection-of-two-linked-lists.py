# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        count1 = 0
        count2 = 0

        slowA = headA
        slowB = headB

        while slowA:
            count1+=1
            slowA = slowA.next
        
        while slowB:
            count2+=1
            slowB = slowB.next
        while count1>count2:
            headA =headA.next
            count1-=1
        while count2>count1:
            headB = headB.next
            count2-=1
        while headA and headB:
            if headA==headB:
                return headA
            headA = headA.next
            headB = headB.next
        


        


        