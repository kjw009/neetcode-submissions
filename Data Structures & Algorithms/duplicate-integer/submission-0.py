from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map = Counter(nums)
        
        for key in count_map:
            print(key, count_map[key])
            if count_map[key] > 1:
                return True
        return False
        