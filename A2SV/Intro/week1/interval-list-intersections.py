class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 = 0 
        p2 = 0
        res = []

        while p1 < len(firstList) and p2 < len(secondList):
            f_s, f_e = firstList[p1][0], firstList[p1][1]
            e_s, e_e = secondList[p2][0], secondList[p2][1]
            maxS = max(f_s, e_s)
            minE = min(f_e, e_e)
            if maxS <=  minE:
                res.append([maxS, minE])
            if f_e <= e_e:
                p1 += 1 
            else:
                p2 += 1 

        return res
        
