class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        backlog = set()
        for i in nums:
            if i in backlog:
                return True
            backlog.add(i)
        return False

        