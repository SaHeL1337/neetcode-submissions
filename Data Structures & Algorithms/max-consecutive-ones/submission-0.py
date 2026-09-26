class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutiveOnes = 0
        maxConsecutiveOnes = 0
        for i in nums:
            if i == 1:
                consecutiveOnes += 1
            else:
                maxConsecutiveOnes = max(maxConsecutiveOnes,consecutiveOnes)
                consecutiveOnes = 0

        return max(maxConsecutiveOnes,consecutiveOnes)
