from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq_map = Counter(s)

        for ch in t:
            if s_freq_map[ch] > 0:
                s_freq_map[ch] = s_freq_map.get(ch) - 1
            elif s_freq_map[ch] <= 0:
                return False
        return sum(s_freq_map.values()) == 0

        