from collections import counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        def is_anagram(c1, c2):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if c1[ch] != c2[ch]:
                    return False
            return True
        
        p_len = len(p)
        s_len = len(s)
        
        if p_len > s_len:
            return []
        
        p_counter = counter(p)
        s_counter = counter(s[:p_len])
        
        result = []
        
        if is_anagram(p_counter, s_counter):
            result.append(0)
        for i in range(1, s_len - p_len + 1):
            if s[i-1] != s[i+p_len-1]:
                s_counter[s[i-1]] -=1
                s_counter[s[i+p_len-1]] += 1
                
            if is_anagram(p_counter, s_counter):
                result.append(i)
                        
        return result
        