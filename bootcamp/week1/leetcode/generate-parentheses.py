class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        candidates = ['(',')']
        ans = []

        def backtrack(i,path,s = 0,r = 0):
            if len(path)==2*n:
                ans.append(''.join(path[:]))
                return
            for j in range(2):
                if candidates[j]=='(' and s==n:
                    continue
                if candidates[j]==')' and s<r+1:
                    continue
                path.append(candidates[j])
                if candidates[j]=='(':
                    backtrack(j,path,s+1,r)
                else:
                    backtrack(j,path,s,r+1)
                path.pop()
                
        backtrack(0,[])
        return ans
        