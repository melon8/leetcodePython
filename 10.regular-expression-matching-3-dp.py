class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] 代表 s[i:] 和 p[j:] 是否匹配。
        # 因为两字符串可以各自为空，所以i的范围是[0, len(s)], j的范围是[0, len(p)]
        dp = [[False]*(len(p) + 1) for _ in range(len(s) + 1)]
        dp[len(s)][len(p)] = True
        
        
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = False
                if i < len(s): 
                    first_match = p[j] in {s[i], "."}
                if j + 2 <= len(p) and p[j+1] == '*':
                    dp[i][j] = first_match and dp[i+1][j] or dp[i][j+2]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        
        return dp[0][0]
                    