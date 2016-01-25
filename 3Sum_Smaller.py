class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        count, k = 0, 2
        while k < n:
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] + nums[k] >= target:
                    j -= 1
                else:
                    count += j-i
                    i += 1
            k += 1
        return count
