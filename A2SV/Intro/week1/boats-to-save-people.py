class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        right = len(people)-1
        left = 0
        ans = 0

        while right>=left:

            if people[right]+people[left]<=limit:
                left+=1
            ans+=1
            right-=1
        return ans




        
        