class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        ans = len(cards)+1
        left = 0
        seen = defaultdict(int)

        for right in range(len(cards)):

            while seen[cards[right]]==1:
                seen[cards[left]]-=1

                if seen[cards[left]]==0:
                    seen.pop(cards[left])
                ans = min(ans,right-left+1)
                left+=1
            seen[cards[right]]+=1
        return ans if ans!=len(cards)+1 else -1

        