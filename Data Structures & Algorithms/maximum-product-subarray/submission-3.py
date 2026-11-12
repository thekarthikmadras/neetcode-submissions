class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = 1
        curMin = 1
        for num in nums:
            temp = curMax * num
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(temp, curMin * num, num)
            res = max(res, curMax)
        return res

