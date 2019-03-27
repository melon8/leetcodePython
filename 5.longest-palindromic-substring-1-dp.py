class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        
        #dp dp[i][j]:  代表si~sj子串是否一个回文，答
        dp = [[False]* len(s) for _ in range(len(s))]
        max_len_i = max_len_j = 0
        
        #base case
        for i in range(len(s)):
            dp[i][i] = True
            if i+1 < len(s):
                dp[i][i+1] = s[i] == s[i+1]
                if dp[i][i+1]:
                    max_len_i, max_len_j = i, i+1
        # form dp
        for j in range(2, len(s)):
            for i in range(j-1):
                # 递推公式
                dp[i][j] =  dp[i+1][j-1] and (s[i] == s[j])
                
                # 更新最长回文子串头尾下标
                if dp[i][j] and (j - i > max_len_j - max_len_i):
                    max_len_i, max_len_j = i, j   

        return s[max_len_i:max_len_j+1]