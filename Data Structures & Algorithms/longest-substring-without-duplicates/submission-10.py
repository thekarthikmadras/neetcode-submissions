class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        res = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] in mp:
                l = max(mp[s[r]]+1, l)
            res = max(r - l + 1, res)
            mp[s[r]] = r
            r += 1
        return res