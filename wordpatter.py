class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        map_p_s = {}
        map_s_p = {}
        for ch_p , ch_s in zip(pattern , words):
            if ch_p in map_p_s:
                if map_p_s[ch_p] != ch_s:
                    return False
            else:
                map_p_s[ch_p] = ch_s

            if ch_s in map_s_p:
                if map_s_p[ch_s] != ch_p:
                    return False
            else:
                map_s_p[ch_s] = ch_p
                    
        return True
