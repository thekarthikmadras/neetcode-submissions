class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in prevMap:
                return [prevMap[compliment], i]
            else:
                prevMap[num] = i