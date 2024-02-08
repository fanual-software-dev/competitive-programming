class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        impact = [0]*(len(nums)+1)
        for request in requests:
            impact[request[0]]+=1
            impact[request[1]+1]-=1
        for i in range(1,len(impact)):
            impact[i]+=impact[i-1]
        impact_dict = defaultdict(list)
        for i in range(len(impact)-1):
            impact_dict[impact[i]].append(i)
        new = [i for i in impact_dict.keys()]
        new.sort()
        ans = [-1]*len(nums)
        addis = sorted(nums)[::-1]
        for i in new:
            while impact_dict[i]:
                v = impact_dict[i].pop()
                ans[v]=addis.pop()
        for i in range(len(ans)):
            if ans[i]==-1:
                ans[i]=addis.pop()
        final_ans = [0]*(len(nums)+1)
        for i in range(len(ans)):
            final_ans[i+1]=ans[i]+final_ans[i]
        result = 0
        for i in requests:
            result+=final_ans[i[1]+1]-final_ans[i[0]]
        return result%(10**9+7)