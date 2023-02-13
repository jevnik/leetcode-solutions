def runningSum(nums):
    res = [None] * len(nums)        
    res[0] = nums[0]
    
    for x in range(1,len(nums)):
        res[x]=nums[x]+res[x-1]
    return res