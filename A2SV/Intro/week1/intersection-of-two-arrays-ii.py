class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []

        dict1 = [0]*(max(max(nums1),max(nums2))+1)
        dict2 = [0]*(max(max(nums1),max(nums2))+1)

        for i in nums1:

            dict1[i] += 1

        for i in nums2:

            dict2[i] += 1
        
        for i in nums1:

            if dict1[i]>0 and dict2[i]>0 and i not in ans:

                for j in range(min(dict1[i],dict2[i])):
                    ans.append(i)
         

        return ans