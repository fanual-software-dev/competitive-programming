class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        ans_dict = {}

        for i in range(len(nums)):

            ans_dict[nums[i]] = i

        for operation in operations:

            ans_dict[operation[1]] = ans_dict.get(operation[0])

            ans_dict.pop(operation[0])
            
        ans_arr=[0]*len(ans_dict.keys())

        for key,value in ans_dict.items():
            
            ans_arr[value] = key
        
        return ans_arr
        