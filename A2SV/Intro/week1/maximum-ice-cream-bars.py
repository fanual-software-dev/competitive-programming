class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        count_arr = [0]*(max(costs)+1)

        for i in costs:
            count_arr[i]+=1
        
        total = 0
        
        
        for i in range(len(count_arr)):
            left = count_arr[i]
            while left and  coins - i>=0 :
                total+=1
                coins-=i
                left-=1
        return total

        