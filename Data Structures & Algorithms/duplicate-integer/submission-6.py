class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for num in nums:
            if num not in res:
                res.add(num)
            else:
                return True
        return False