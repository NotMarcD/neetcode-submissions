class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 0
        k = 1
        for i in range (len(nums)): 
            if nums[ptr] != nums[i]:
                ptr += 1
                nums[ptr] = nums[i]
                k += 1

        return k