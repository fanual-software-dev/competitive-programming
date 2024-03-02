class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashmap = {'2':['a','b','c'],'3':['d','e','f'],
        '4':['g','h','i'],'5':['j','k','l'],
        '6':['m','n','o'],'7':['p','q','r','s'],
        '8':['t','u','v'],'9':['w','x','y','z']}
        length = len(digits)
        ans = []

        def backtrack(i,path,k = 0):

            if len(path)==length:
                ans.append(''.join(path[:]))
                return
            for j in range(i,length):
                for k in range(len(hashmap[digits[i]])):
                    path.append(hashmap[digits[i]][k])
                    backtrack(j+1,path,k+1)
                    path.pop() 
        backtrack(0,[])
        return ans
        