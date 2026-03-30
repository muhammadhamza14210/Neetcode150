class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        for i in range(len(s)):
            dic_s[s[i]] = 1 + dic_s.get(s[i],0)
        
        for i in range(len(t)):
            dic_t[t[i]] = 1 + dic_t.get(t[i],0)
        
        return dic_s == dic_t