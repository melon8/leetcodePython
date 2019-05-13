class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 记忆化搜索，过程和recursion一样，增加了一个memo存储已经算过的状态，避免重复计算
        # key:元组(index of s, index of p), value: isMatch：bool
        memo = {}
        #i:s的index； j: p的index
        # top  down dp，inner function
        def dpIsMatch(i, j):
            if (i, j) not in memo:
                ans = False
                if j == len(p):
                    ans = i == len(s)
                    
                else:
                    first_match = False
                    if i < len(s) and p[j] in {s[i], "."}:
                        first_match = True

                    if j+1 < len(p) and p[j+1] == '*':
                        ans = dpIsMatch(i, j+2) or (first_match and dpIsMatch(i+1, j))
                    else:
                        ans = first_match and dpIsMatch(i+1, j+1)
                memo[i, j] = ans
            return memo[i, j]
        
        return dpIsMatch(0, 0)
                    
                    