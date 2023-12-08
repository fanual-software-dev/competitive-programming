class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        
        ans_dict = {}

        for match in matches:

            if match[0] in ans_dict:

                ans_dict[match[0]][0] = 1+ ans_dict[match[0]][0]
            
            else:

                ans_dict[match[0]] = [1,0]

            if match[1] in ans_dict:

                ans_dict[match[1]][1] = 1 + ans_dict[match[1]][1]
            
            else:

                ans_dict[match[1]] = [0,1]

        ans = [[],[]]
        
        for key ,value in ans_dict.items():

            if value[0] > 0 and value[1] == 0:

                ans[0].append(key)

            elif value[1]==1:

                ans[1].append(key)
        return [sorted(ans[0]), sorted(ans[1])]