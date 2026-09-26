class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l, r = 0, 0 
        res = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]]+1, l)
            res = max(res, r - l + 1)
            mp[s[r]] = r
        return res