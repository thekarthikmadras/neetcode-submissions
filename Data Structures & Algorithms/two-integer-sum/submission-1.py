class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, n in enumerate(nums):
            compliment = target - n
            if compliment in res:
                return [res[compliment], i]
            else:
                res[n] = i 
        