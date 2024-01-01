class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        ans_dict = {}

        for i in nums:

            ans_dict[i] = 1 + ans_dict.get(i,0)
        
        ans =[]

        for key in ans_dict.keys():

            ans.append(key)
        ans.sort()
        total = 0
        operations = 0
        
        for i in range(len(ans)-2,-1,-1):

            operations += total + ans_dict.get(ans[i+1])
            total+= ans_dict.get(ans[i+1])
            
        

        return operations
        