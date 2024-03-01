class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        n = [i for i in range(1,n+1)]
        ans = []
        def backtrack(n,k,path = []):

            if len(path)==k:
                ans.append(path[:])

            for i in range(len(n)):
                path.append(n[i])
                new = n[i+1:]
                backtrack(new,k)
            if path:path.pop()
        backtrack(n,k)
        return ans

        