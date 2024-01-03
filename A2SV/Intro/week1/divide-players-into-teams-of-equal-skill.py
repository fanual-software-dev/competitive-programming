class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()
        ans , chemistry = skill[0]+skill[len(skill)-1] , skill[0]*skill[len(skill)-1]
        left , right = 1 , len(skill)-2

        while left<right:

            if skill[left] + skill[right] == ans:

                chemistry+=(skill[left]*skill[right])
            else:
                return -1
            left+=1
            right-=1
            
        return chemistry