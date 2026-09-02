class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       hset = set(nums)
       max_streak = 0

       for num in nums:
        if num - 1 not in hset:
            streak = 1
            while num + streak in hset:
                streak += 1 
            max_streak = max(max_streak, streak)
       return max_streak