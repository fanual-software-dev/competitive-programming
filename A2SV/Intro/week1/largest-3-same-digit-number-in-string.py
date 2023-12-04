class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        ans=""
        left=0
        l=num[0]
        for i in range(len(num)):
            if num[i]!=l:
                l=num[i]
                left=i
            if not ans and i-left+1==3:
                    ans=num[left:i+1]
            elif i-left+1==3 and ans<num[left:i+1]:
                ans=num[left:i+1]
        return ans
            

        