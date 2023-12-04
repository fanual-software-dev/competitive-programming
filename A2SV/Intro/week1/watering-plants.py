class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        total=0
        n=capacity
        for i in range(len(plants)):
            n-=plants[i]
            if n>=0:
                total+=1
            else:
                total+=((i)*2)+1
                n=capacity-plants[i]
        return total