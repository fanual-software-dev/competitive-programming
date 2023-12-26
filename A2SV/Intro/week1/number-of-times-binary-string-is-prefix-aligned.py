class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:

        ans = 0
        total1 = 0
        sum2 = 0
        for i in range(len(flips)):

            total1+=i
            sum2+=(flips[i]-1)

            if total1==sum2:
                ans+=1
        return ans