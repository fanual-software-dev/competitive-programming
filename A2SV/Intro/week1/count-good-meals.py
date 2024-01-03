class Solution:
    def countPairs(self, d: List[int]) -> int:

        ans_dict = Counter(d)
        ans = 0

        def binary(target):
            left = 0
            right = 20

            while left<=right:

                mid = (left+right)//2

                if 2**mid>target:
                    right = mid-1
                else:
                    left = mid+1
            return 2**left 
        
        for i in set(d):

            if i!=0 and binary(i)-i!=i and binary(i)-i  in ans_dict:
                ans+=(ans_dict[binary(i)-i]*ans_dict[i])
                
            elif binary(i)-i==i:
                
                if i  in ans_dict and ans_dict[i]>1:
                    ans+=((ans_dict[i]-1)*ans_dict[i])//2
                    
                if 0 in ans_dict:
                    ans+=(ans_dict[0]*ans_dict[i])

            
        
        return ans%(10**9+7)