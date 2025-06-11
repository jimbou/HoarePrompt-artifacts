#State of the program right berfore the function call: nums is a list of non-negative integers, the sum of the integers in nums is divisible by the length of nums.
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns the string 'NO'
    #State: *nums is a list of non-negative integers, n is the length of nums, total is the sum of the integers in nums, and total is divisible by n
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: nums is a list of non-negative integers, n is the length of nums, total is the sum of the integers in nums, total is divisible by n, mean is the mean of the integers in nums, curr is the sum of the integers in nums minus n times the mean, i is n, and curr is greater than or equal to 0
    return 'YES'
    #The program returns the string 'YES'

#Overall this is what the function does:Determines if a list of non-negative integers can be rearranged to have a specific mean, returning 'YES' if possible and 'NO' otherwise.

