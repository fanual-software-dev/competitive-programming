class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """

        ans = []

        left = 0

        for i in spaces:

            ans.append(s[left:i]+" ")
            left = i
        ans.append(s[left:])

        return "".join(ans)
        