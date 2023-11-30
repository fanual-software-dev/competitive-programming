class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for j in range(len(matrix)-1):

            for i in range(len(matrix[j])):
                for k in range(j+1,len(matrix)):
                    if i+k-j>=len(matrix[k]):
                        continue
                    elif matrix[j][i]!=matrix[k][i+k-j]:
                        return False
        return True