class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        def helper(s, l, r):
            nonlocal resIdx, resLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < r - l + 1:
                    resLen = r - l + 1
                    resIdx = l
                l -= 1
                r += 1
            return resIdx, resLen

        for i in range(len(s)):
            # odd
            helper(s, i, i)
            #even
            helper(s, i, i + 1)
        return s[resIdx: resIdx + resLen]


        

