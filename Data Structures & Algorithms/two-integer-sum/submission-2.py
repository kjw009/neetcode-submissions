class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # val => index
        hash = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash:
                return [hash[diff], i]
            hash[num] = i
          


        