class Solution:
    def minSteps(self, s: str, t: str) -> int:
        seen1,seen2 = Counter(s),Counter(t)  
        step = 0
        
        for i in seen1:

            if i in seen2:
                if seen2[i]<seen1[i]:
                    step+=seen1[i]-seen2[i]
            else:
                step+=seen1[i]
        return step
        