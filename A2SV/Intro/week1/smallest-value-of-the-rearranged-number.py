class Solution:
    def smallestNumber(self, num: int) -> int:

        ans = []
        negative = False
        count = 0
        for i in str(num):

            if i == "-":

                negative = True
            else:ans.append(i)

            if i == "0":
                count+=1
        
        ans.sort()

        if negative:

            return 0 - int("".join(ans[::-1]))
        
        if count:

            for i in range(len(ans)):

                if ans[i]>"0":
                    ans[0],ans[i] = ans[i],ans[0]
                    break
        return int("".join(ans))
        