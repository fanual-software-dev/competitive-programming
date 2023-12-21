class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        remainder = 1
        l =len(digits)-1
        sumo = 0
        while l>-1 and remainder>0:

            sumo = digits[l] + 1

            if sumo >= 10:

                digits[l] = 0
            else:

                digits[l] = sumo
                remainder = 0
                sumo = 0
            l-=1
        return [1]+digits if remainder else digits
            
        