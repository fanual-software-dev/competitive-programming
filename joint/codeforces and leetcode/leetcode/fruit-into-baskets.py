class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        seen = {}
        left = total = 0
        for right in range(len(fruits)):
            while left<=right and fruits[right] not in seen and len(seen.keys())==2:
                seen[fruits[left]]-=1
                if seen[fruits[left]]==0:
                    seen.pop(fruits[left])
                left+=1
            seen[fruits[right]] = 1 + seen.get(fruits[right],0)
            total = max(total,right-left+1)
        return total 