class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        for i in range(len(s)):
            dic_s[s[i]] = s.count(s[i])
        
        for i in range(len(t)):
            dic_t[t[i]] = t.count(t[i])
        
        return dic_s == dic_t