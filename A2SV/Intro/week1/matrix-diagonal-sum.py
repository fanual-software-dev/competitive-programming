class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        if len(mat)==1:
            return mat[0][0]

        ans = 0

        v = [0,0]
        v_ = [0,len(mat)-1]

        for i in range(len(mat)):

            if v!=v_:
                ans+= mat[v[0]][v[1]]
                ans+= mat[v_[0]][v_[1]]
            else:
                ans+= mat[v[0]][v[1]]

            v[0],v[1] = v[0]+1,v[1]+1
            v_[0],v_[1] = v_[0]+1,v_[1]-1
            
        
        
        return ans
        