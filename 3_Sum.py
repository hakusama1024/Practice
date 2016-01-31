def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    size = len(nums)
    if size == 0 : return res
    nums.sort()
    for i in range(size-2):
        target = -nums[i]
        l = i+1; r = size-1
        while l < r:
            if nums[l]+nums[r] == target:
                tmp = [nums[i], nums[l], nums[r]]
                if tmp not in res:
                    res.append(tmp)
                l+=1
            elif nums[l]+nums[r] < target:
                l += 1
            else:
                r -= 1
	res.sort()
    print res

numsl = [-1, 0, 1, 2, -1, -4, -2, 6]
threeSum(numsl)
