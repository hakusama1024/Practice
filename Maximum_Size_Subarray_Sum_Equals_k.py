class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0 : return 0
        acc = 0
        res = 0
        d = {0 : -1}
        for i in range(len(nums)):
            acc += nums[i]
            if acc not in d:
                d[acc] = i
            if acc - k in d:
                res = max(res, i - d[acc-k])
        return res
                
        
