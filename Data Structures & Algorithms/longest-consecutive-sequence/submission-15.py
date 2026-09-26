class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0
        maxCount = 0
        for num in nums:
            if (num - 1) not in nums:
                count = 1
                while num + count in nums:
                    count += 1
                maxCount = max(maxCount, count)
        return maxCount