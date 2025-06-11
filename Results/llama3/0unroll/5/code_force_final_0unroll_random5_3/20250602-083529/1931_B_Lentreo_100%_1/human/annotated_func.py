#State of the program right berfore the function call: nums is a list of non-negative integers, the sum of nums is divisible by the length of nums.
    n = len(nums)
    total = sum(nums)
    if (total % n != 0) :
        return 'NO'
        #The program returns the string 'NO'
    #State: *n is the length of the list nums, total is a multiple of n equal to the sum of all elements in nums, nums is a list of non-negative integers. The total is a multiple of n
    mean = total // n
    curr = 0
    for i in range(n):
        curr += nums[i] - mean
        
        if curr < 0:
            return 'NO'
        
    #State: Output State: n is the length of the list nums, total is a multiple of n equal to the sum of all elements in nums, nums is a list of non-negative integers, mean is the average of the elements in nums, curr is the sum of the differences between each element in nums and the mean, or 'NO' if the sum of these differences is negative at any point.
    return 'YES'
    #The program returns 'YES'

#Overall this is what the function does:Determines if a list of non-negative integers can be rearranged to have a specific average value. The function takes a list of non-negative integers as input and returns 'YES' if the list can be rearranged to have the average value equal to the sum of the elements divided by the length of the list, and 'NO' otherwise. The function checks if the sum of the elements is divisible by the length of the list and if the cumulative sum of the differences between each element and the mean is never negative.

