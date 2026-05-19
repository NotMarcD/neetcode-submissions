class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        ptr = 0
        for i in range(len(nums)):
            if nums[i] != val: 
                nums[ptr] = nums[i]
                ptr += 1
                k += 1
        
        return k