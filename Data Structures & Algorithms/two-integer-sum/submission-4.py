class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in prev:
                prev[nums[i]] = i
            else:
                return [prev[diff], i]
            
            
