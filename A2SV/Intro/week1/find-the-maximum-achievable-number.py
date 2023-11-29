class Solution(object):
    def theMaximumAchievableX(self, num, t):
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        ans=0
        for i in range(num-2*t,num+2*t+1):
            num2=num
            j=i
            
            if i<num:
                u=t
                while u>0:
                    j+=1
                    num2-=1
                    u-=1
                    if j==num2:
                        ans=max(ans,i)
                        
            elif i>num:
                u=t
                while u>0:
                    j-=1
                    num2+=1
                    u-=1
                    if j==num2:
                        ans=max(ans,i)
                         
        return ans
        