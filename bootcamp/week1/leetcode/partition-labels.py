class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        seen = Counter(s)
        ans = []
        count = 0
        newseen = {}
        for i in range(len(s)-1,-1,-1):
            seen[s[i]]-=1
            count+=seen[s[i]]-newseen.get(s[i],0)
            newseen[s[i]] = 1 + newseen.get(s[i],0) 
            
            if count<=0:
                ans.append(sum(newseen.values()))
                newseen = {}
                count = 0
        return ans[::-1]

            