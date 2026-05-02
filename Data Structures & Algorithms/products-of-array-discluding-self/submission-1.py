class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []

        for i, num in enumerate(nums):
            rem = [n for n in nums]
            rem.pop(i)
            res = 1
            for j in range(len(rem)):
                res *= rem[j]
            output.append(res)
        return output
