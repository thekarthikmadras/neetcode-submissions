class Solution:
    def numDecodings(self, s: str) -> int:
        dp1, dp2 = 1, 0  # dp[i+1], dp[i+2]
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp = 0
            else:
                dp = dp1  # single-digit decode
                
                # check for valid two-digit decode
                if i + 1 < len(s) and (s[i] == '1' or
                   (s[i] == '2' and s[i + 1] in '0123456')):
                    dp += dp2
            
            # move window
            dp2, dp1 = dp1, dp
        
        return dp1
