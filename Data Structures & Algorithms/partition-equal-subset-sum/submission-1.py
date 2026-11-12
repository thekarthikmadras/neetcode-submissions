class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums)):
            nextDP = set()
            for t in dp:
                if nums[i] + t == target:
                    return True
                nextDP.add(nums[i] + t)
                nextDP.add(t)
            dp = nextDP
        return False
