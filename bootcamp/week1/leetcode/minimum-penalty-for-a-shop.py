class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y_sum = [0]*(len(customers)+1)
        n_sum = [0]*(len(customers)+1)

        for i in range(len(customers)):
            if customers[i]=="Y":
                y_sum[i+1] = y_sum[i]+1
                n_sum[i+1] = n_sum[i]
            else:
                y_sum[i+1] = y_sum[i]
                n_sum[i+1] = n_sum[i] + 1
        ans = float('inf')
        result = 0
        for i in range(len(customers)+1): 
            if ans>y_sum[-1]-y_sum[i] + n_sum[i]:
                result = i
                ans = y_sum[-1]-y_sum[i] + n_sum[i] 
        return result    