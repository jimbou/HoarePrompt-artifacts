#State of the program right berfore the function call: nums is a list of non-negative integers, the sum of the integers in nums is divisible by the length of nums.
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns the string 'NO'.
    #State: *nums is a list of non-negative integers, n is the length of nums, total is the sum of the integers in nums, the sum of the integers in nums is divisible by the length of nums, and the remainder of the division of the sum of the integers in nums by the length of nums is 0
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: Output State: nums is a list of non-negative integers, n is the length of nums, total is the sum of the integers in nums, mean is the sum of the integers in nums divided by the length of nums, and curr is the sum of the differences between each integer in nums and the mean.
    return 'YES'
    #The program returns the string 'YES'

#Overall this is what the function does:Determines whether a list of non-negative integers can be rearranged to have a mean equal to the sum of the integers divided by the length of the list, returning 'YES' if possible and 'NO' otherwise.

