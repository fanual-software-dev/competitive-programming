# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        leng = 0
        temp = head
        ans = []
        while temp:
            leng+=1
            temp = temp.next
        original = k
        k=leng if k>=leng else k
        r = leng%k if k>0 else 0
        leng = leng//k if k>0 else 0
        count = 0
        dumy = head
        while head:
            count+=1
            c = 0 if r<=0 else 1
            if count==leng+c:
                ans.append(dumy)
                temp = head.next
                head.next = None
                head = temp
                dumy = head
                count = 0
                r-=1
            else:
                head = head.next
        while len(ans)!=original:
            ans.append(dumy)
        return ans
        