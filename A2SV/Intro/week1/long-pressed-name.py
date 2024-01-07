class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        left=0
        prev = name[left]
        for right in range(len(typed)):

            if typed[right]!=name[left] and typed[right]!=prev:

                return False
            elif typed[right]!=name[left] and typed[right] == prev:
                continue
            elif typed[right]==name[left]:

                prev = name[left]
                if left<len(name)-1:
                    left+=1
                
    
        return left==len(name)-1 and name[-1]==typed[-1]
