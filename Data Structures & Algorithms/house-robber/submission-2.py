class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for num in nums:
            temp = rob1
            rob1 = max(num + rob2, rob1)
            rob2 = temp
        return rob1