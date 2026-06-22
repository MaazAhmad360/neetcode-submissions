class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0
        maxRes = 0

        l, r = 0, 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
                res += 1
            else:
                if res > maxRes:
                    maxRes = res
                while l < len(s) and s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                    res -= 1
                l += 1
                r += 1
        if res > maxRes:
                    maxRes = res
        return maxRes