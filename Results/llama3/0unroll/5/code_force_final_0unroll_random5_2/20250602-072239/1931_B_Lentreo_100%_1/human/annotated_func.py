#State of the program right berfore the function call: nums is a list of non-negative integers, the sum of nums is divisible by the length of nums.
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns the string 'NO'
    #State: *nums is a list of non-negative integers, n is the length of nums, total is the sum of nums, the sum of nums is divisible by the length of nums, and the remainder of the division of the sum of nums by the length of nums is 0
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: Output State: The final value of curr is the sum of the differences between each number in the list and the mean, and the function returns 'NO' if curr is ever less than 0, otherwise it returns None. The values of nums, n, total, and mean remain unchanged.
    return 'YES'
    #The program returns 'YES'

#Overall this is what the function does:Determines if a list of non-negative integers can be rearranged to have a specific mean value.

