class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five,ten,twenty = 0,0,0
        if bills[0]!=5:
            return False
        for bill in bills:
            if bill==5:
                five+=1
            elif bill==10:
                if five:
                    five-=1
                    ten+=1
                else:
                    return False
            elif bill==20:
                if not five:
                    return False
                if ten:
                    ten-=1
                    five-=1
                
                elif not ten and five>=3:
                    five-=3
                else:
                    return False
        return True
         
        