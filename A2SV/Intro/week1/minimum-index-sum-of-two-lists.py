class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        dict1 = {}
        mins = 20001
        ans = []

        for i in range( len( list1 ) ):

            dict1[list1[i]]=i

        

        for i in range(len(list2)):

            if dict1.get(list2[i],-1)!=-1 :

                mins = min(mins,i + dict1.get( list2[i] ) )

                dict1[list2[i]] = i + dict1.get( list2[i] ) + 5000
        

        for key, value in dict1.items():

            if value >= 5000 and value - 5000 == mins:

                ans.append( key )

        return ans