class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        left = 0
        
        for num in nums2:

            while left<len(nums1):

                if nums1[left]<num:
                    left+=1
                elif nums1[left] == num:
                    return num
                else:
                    break
        return -1        