class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ans=[]
        i=0
        while i <len(command):

            if command[i]=="G":
                ans.append("G")
            elif command[i]=="(" and command[i+1]==")":
                ans.append("o")
            elif command[i]=="(" and command[i+1]=="a":
                ans.append("al")
            i+=1
        return "".join(ans)