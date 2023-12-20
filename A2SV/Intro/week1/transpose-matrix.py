class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        matrixans=[[] for i in range(len(matrix[0]))]

        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                matrixans[i].append(matrix[j][i])
        return matrixans
        