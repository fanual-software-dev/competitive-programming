class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        mx = max(arr1)
        ans = [0]*(mx+1)

        for i in arr1:
            
            ans[i]+=1
        arr = []

        for i in arr1:

            if i not in arr2:
                arr.append(i)
        left = 0
        for i in arr2:

            for j in range(ans[i]):

                arr1[left] = i
                left+=1
        arr1[left:] = sorted(arr)
        return arr1

        