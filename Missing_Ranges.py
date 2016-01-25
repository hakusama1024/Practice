class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums = [lower-1] + nums + [upper+1]
        res = []
        pre = lower-1
        for cur in nums:
            if cur - pre == 2:
                res.append(str(pre+1))
            elif cur - pre > 2:
                res.append(str(pre+1) + '->' + str(cur-1))
            pre = cur
    
        return res
