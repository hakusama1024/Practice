class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return 
        size = len(nums)
        for i in range(1, size, 2):
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
            if i + 1 < size and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]


