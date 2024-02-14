class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        seen = Counter(answers)
        total_rabbits = 0
        for key in seen:
            total_rabbits += ceil(seen[key] / (key + 1)) * (key + 1)
        return total_rabbits
