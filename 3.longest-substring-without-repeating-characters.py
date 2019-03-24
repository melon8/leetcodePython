# 时间复杂度 O(n)
# 步骤
# 1. window的右指针遍（j）历字符串 
# 当右指针指向的字符在 hashmap 中已存在，则左指针(i)跳到原重复字符的 index + 1，hashmap 更新该重复字符的 index 为 j
# 更新 max length： max(ans, j - i + 1)
# 空间复杂度 O(n) (没有重复的字符时可能会全部放到 hashmap 中)

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