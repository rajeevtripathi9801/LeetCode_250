class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        frequency_map_s = {}
        frequency_map_t = {}

        for i in range(len(s)):
            frequency_map_s[s[i]] = 1 + frequency_map_s.get(s[i], 0)
            frequency_map_t[t[i]] = 1 + frequency_map_t.get(t[i], 0)

        for c in frequency_map_s:
            if frequency_map_s[c] != frequency_map_t.get(c,0):
                return False
        
        return True



