class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        max_len = 0
        
        for num in hset:
            if (num - 1) not in hset:
                curr_num = num
                curr_streak = 1
                
                while (curr_num + 1) in hset:
                    curr_num += 1
                    curr_streak += 1
                
                max_len = max(max_len, curr_streak)

        return max_len