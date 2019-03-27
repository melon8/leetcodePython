# Recursion
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #因为 a* 匹配 0个或多个a，所以s='' p ='a*'仍然算可以匹配，所以p消耗完了才算结束
        if not p:
            return not s
        
        # 首字母是否match
        firstMatch = len(s) > 0 and p[0] in {s[0], "."}
        
        # 如果pattern第二位是*，可能是第一位匹配，则消耗掉s一个字符，p不变 e.g. s = aa,p = a*  
        # 或者第一位不匹配，消耗掉两位p（a*：匹配0个或多个a）e.g. s = b, p = a*
        if len(p) >= 2 and p[1] == "*":
            return firstMatch and self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
        else:
            return firstMatch and self.isMatch(s[1:], p[1:])


            