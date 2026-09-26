class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diff = {}
        index = 0
        for i in nums:
            partnerIndex = diff.get(target - i)
            if partnerIndex is not None:
                return [partnerIndex,index]
            diff[i] = index
            index += 1