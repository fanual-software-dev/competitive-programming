class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        ans = [0]*(len(s)+1)
        seen = {i:chr(96+i) for i in range(1,27)}
        seen1 = {seen[i]:i for i in seen}
        
        for start,end,shift in shifts:
            if shift==0:
                ans[start]-=1
                ans[end+1]+=1
            else:
                ans[start]+=1
                ans[end+1]-=1
        for i in range(1,len(ans)):
            ans[i]+=ans[i-1]
        shifted = [i for i in s]
        for i in range(len(s)):
            if seen1[shifted[i]]+ans[i]>=1:
                if (seen1[shifted[i]]+ans[i])%26!=0:
                    shifted[i] = seen.get((seen1[shifted[i]]+ans[i])%26)
                else:shifted[i] = 'z'
            elif seen1[shifted[i]]+ans[i]<1:
                p = abs(seen1[shifted[i]]+ans[i])%26
                shifted[i] = seen[26-p]
        return "".join(shifted)
        