class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_cnt, t_cnt = {}, {}
        for i in range(len(s)):
            s_cnt[s[i]] = 1 + s_cnt.get(s[i], 0)
            t_cnt[t[i]] = 1 + t_cnt.get(t[i], 0)
        return s_cnt == t_cnt