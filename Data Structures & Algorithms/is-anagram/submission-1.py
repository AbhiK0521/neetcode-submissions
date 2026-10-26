class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sVals = {}
        tVals = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            currS = s[i]
            currT = t[i]
            if currS in sVals:
                sVals[currS] = 1 + sVals[currS]
            else:
                sVals[currS] = 1
            
            if currT in tVals:
                tVals[currT] = 1 + tVals[currT]
            else:
                tVals[currT] = 1


        for j in s:
            if not j in tVals and j in sVals:
                return False
            else:
                if sVals[j] != tVals[j]:
                    return False
        
        return True
        
        
                
                