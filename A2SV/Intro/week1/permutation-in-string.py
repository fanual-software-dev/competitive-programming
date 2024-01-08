class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False

        ans = Counter(s1)
        seen = {}
        left = 0

        for right in range(len(s2)):
            if s2[right] not in ans:
                seen = {}
                left = right+1
            else:
                seen[s2[right]] = 1 +seen.get(s2[right],0) 

            if right-left+1 == len(s1):
                if ans==seen:
                    return True
                seen[s2[left]]-=1
                if seen[s2[left]]==0:
                    seen.pop(s2[left])
                left+=1

        return False