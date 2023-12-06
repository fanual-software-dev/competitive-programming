class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """

        ans_array=[]

        for i in range(len(boxes)):
            
            total_move = 0
            l=0

            while l<len(boxes):

                if boxes[l] == "1":

                    total_move+=abs(i-l)
                l+=1
            ans_array.append(total_move)

        return ans_array
                