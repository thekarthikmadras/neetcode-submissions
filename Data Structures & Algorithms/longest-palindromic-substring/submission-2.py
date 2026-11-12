class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen, resIdx = 0, 0
        def helper(s, l, r, resLen, resIdx):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < r - l + 1:
                    resLen = r - l + 1
                    resIdx = l
                l -= 1
                r += 1
            return resLen, resIdx
        
        for i in range(len(s)):
            resLen, resIdx = helper(s, i, i, resLen, resIdx)
            resLen, resIdx = helper(s, i, i + 1, resLen, resIdx)
        
        return s[resIdx: resIdx + resLen]

