class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        ans_dict = {}
        ans = 0

        for i in nums:

            if k-i in ans_dict:

                ans+=1
                ans_dict[k-i]-=1

                if ans_dict[k-i] == 0:
                    ans_dict.pop(k-i)
                    
            else: ans_dict[i] = 1+ ans_dict.get(i,0)
        return ans



        