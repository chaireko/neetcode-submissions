class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        res = 0
        charSet = set()
        for p2 in range(len(s)):
            while s[p2] in charSet:
                charSet.remove(s[p1])
                p1+=1
            charSet.add(s[p2])
            res = max(res, p2-p1+1)
        return res