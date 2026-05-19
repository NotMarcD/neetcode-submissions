class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            other_num = target - nums[i]
            if other_num in nums and nums.index(other_num) != i:
                return [min(i, nums.index(other_num)), max(i, nums.index(other_num))]