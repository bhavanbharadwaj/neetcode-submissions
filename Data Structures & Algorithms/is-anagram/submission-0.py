class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dictionary = {}
        t_dictionary = {}

        for i in range(len(s)):
            s_dictionary[s[i]] = s_dictionary.get(s[i], 0) + 1
            t_dictionary[t[i]] = t_dictionary.get(t[i], 0) + 1
        
        for key in s_dictionary.keys():
            if key not in t_dictionary:
                return False
            if s_dictionary[key] != t_dictionary[key]:
                return False
        
        return True
        
        