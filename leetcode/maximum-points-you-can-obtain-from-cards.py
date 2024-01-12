class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        if k==len(cardPoints):
            return sum(cardPoints)

        n=len(cardPoints)-k
        left = 0
        right = 0
        ans = float('inf')
        total=0

        while right<len(cardPoints):

            total+=cardPoints[right]

            if right-left+1==n:
                ans = min(ans,total)
                total-=cardPoints[left]
                left+=1
            right+=1
        return sum(cardPoints)-ans
            
        





        