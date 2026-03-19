class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen = {}
        for ch in magazine:
            seen[ch] = seen.get(ch , 0)+1
            
        for alf in ransomNote:
            if alf not in seen or seen[alf] == 0:
                return False
            seen[alf] -= 1
        return True
                
        
