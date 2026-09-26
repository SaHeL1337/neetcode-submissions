class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        backlog = []
        for i in nums:
            if i in backlog:
                return True
            backlog.append(i)
        return False

        