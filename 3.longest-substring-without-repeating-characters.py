class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #char: index dict, e.g.{"a": 0}
        letterDict = {} 
        
        #index of start of substring
        i = 0 
        ans = 0
        for j, ch in enumerate(s):
            if ch in letterDict:
                i = max(i, letterDict[ch] + 1)
            letterDict[ch] = j
            ans = max(ans, j - i + 1)
        return ans