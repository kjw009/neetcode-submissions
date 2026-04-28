from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_map = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]
        output = []

        for num, count in f_map.items():
            freq[count].append(num)
    
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output
        return output


        