class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        coll=[]
        for i in nums1:
            if nums2.index(i)==len(nums2)-1:
                coll.append(-1)
            else:
                for j in nums2[nums2.index(i)+1:]:
                    if j>i:
                        coll.append(j)
                        break
                else:
                    coll.append(-1)
        return coll