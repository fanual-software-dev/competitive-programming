class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        
        for i in range(1,len(heights)):
            
            right = i

            while right>0 and heights[right-1]<heights[right]:

                heights[right-1],heights[right] = heights[right],heights[right-1]
                names[right-1], names[right] =  names[right], names[right-1]
                right-=1
        
        return names
        
        



            
        
        