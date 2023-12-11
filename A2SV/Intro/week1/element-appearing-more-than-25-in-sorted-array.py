class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        ans = arr[0]

        maxcount = 1



        for i in range(1,len(arr)):
            
            if arr[i] == ans:
                maxcount+=1
            else:

                if maxcount > len(arr)/4:
                    
                    return ans

                maxcount = 1

                ans = arr[i]

        return ans
        
        