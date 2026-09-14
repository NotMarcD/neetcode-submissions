class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        post = [0] * len(nums)
        pre_mult = 1
        post_mult = 1

        # prefix array (everything to the left of the current index multiplied)
        for i in range(len(nums)):
            j = -i - 1
            pre[i] = pre_mult
            post[j] = post_mult
            pre_mult *= nums[i]
            post_mult *= nums[j]
        # go through pre and post arrays multiplying the values
        return [l*r for l,r in zip(pre, post)]