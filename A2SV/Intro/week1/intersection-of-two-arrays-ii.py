class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []

        dict1 = {}
        dict2 = {}

        for i in nums1:

            dict1[i] = 1 + dict1.get(i,0)

        for i in nums2:

            dict2[i] = 1 + dict2.get(i,0)
        
        for i in nums1:

            if i in nums2 and i not in ans:

                for j in range(min(dict1[i],dict2[i])):
                    ans.append(i)
         

        return ans