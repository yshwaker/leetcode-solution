class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        pt = 0
        zero_pt = 0  # the position of first zero currently
        count = 0  # the number of zeros
        while pt < len(nums):
            if nums[pt] == 0:
                if count == 0:
                    zero_pt = pt
                count += 1
            else:
                if count > 0:
                    nums[pt], nums[zero_pt] = nums[zero_pt], nums[pt]
                    zero_pt = pt if count == 1 else zero_pt + 1
            pt += 1
