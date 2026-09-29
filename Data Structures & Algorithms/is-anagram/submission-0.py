class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = {}
        t_letters = {}
        if len(s) == len(t):
            for i in range(len(s)):
                s_letters[s[i]] = s_letters.get(s[i], 0) + 1
                t_letters[t[i]] = t_letters.get(t[i], 0) + 1
        else:
            return False
        
        for letter in s:
            if s_letters.get(letter) == t_letters.get(letter):
                continue
            else:
                return False
        
        return True
        
        
                
                