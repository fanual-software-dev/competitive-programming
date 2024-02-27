# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        list1.sort()

        head = Node(list1[0])
        temp = Node(-1,head)

        for i in list1[1:]:
            head.next = Node(i)
            head = head.next
        return temp.next
        