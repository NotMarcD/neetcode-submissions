class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tmp = [[] for _ in range(len(nums) + 1)]
        freq = {}
        result = []

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        for key,value in freq.items():
            tmp[value].append(key)
        
        for index in range(len(tmp) - 1, -1, -1):

            for val in tmp[index]:
                result.append(val) 
                if len(result) == k:
                    return result
