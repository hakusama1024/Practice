class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers : return []
        size = len(numbers)
        left = 0; right = size-1
        while left < right:
            tmp = numbers[left] + numbers[right]
            if tmp == target:
                return [left+1, right+1]
            if tmp < target:
                left += 1
            else:
                right -= 1
        return []
