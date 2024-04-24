class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #solution 1 sorting - O(n log n)
        return sorted(s) == sorted(t)
            
        #solution 2 hashmap - O(n)
        '''if len(s) != len(t):
            return False
        countS, countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True'''

        #solution 3 - use counter
        #return Counter(s) == Counter(t)