class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr) <=2:
            return False
        
        turn = 0
        if arr == sorted(arr) or arr == sorted(arr)[::-1]:
            return False 
        for i in range(1,len(arr)):

            if turn == 1 and arr[i]>=arr[i-1]:

                return False
            if turn == 0 and arr[i]<arr[i-1]:

                turn = 1
            elif turn == 0 and arr[i]==arr[i-1]:
                return False
        return True 

        


        