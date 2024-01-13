class Solution:
    def minSteps(self, s: str, t: str) -> int:
        mega_string = "abcdefghijklmnopqrstuvwxyz"
        steps = 0
        for alphabet in mega_string:
            
            steps += abs( s.count(alphabet) - t.count(alphabet))

        return steps

