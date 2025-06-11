#State of the program right berfore the function call: n is a positive integer, k is a positive integer, nums is a list of n positive integers.
    if (k >= sum(nums)) :
        return n
        #The program returns a positive integer n, which is the number of positive integers in the list nums.
    #State: *n is a positive integer, k is a positive integer, nums is a list of n positive integers. The sum of the elements in nums is larger than k
    a, b = math.ceil(k / 2), k // 2
    ans = 0
    s_a = 0
    s_b = 0
    for i in range(n):
        s_a += nums[i]
        
        s_b += nums[n - i - 1]
        
        if s_a <= a:
            ans += 1
        
        if s_b <= b:
            ans += 1
        
    #State: Output State: n is a positive integer, k is a positive integer, nums is a list of n positive integers, a is the ceiling of k/2, b is the floor of k/2, ans is an integer, s_a is the sum of all elements in nums, s_b is the sum of all elements in nums.
    return ans
    #The program returns ans, which is an integer.

#Overall this is what the function does:This function calculates the maximum number of integers that can be selected from a list of positive integers, such that the sum of the selected integers does not exceed a given target value k. If the sum of all integers in the list is less than or equal to k, it returns the total number of integers in the list. Otherwise, it calculates the maximum number of integers that can be selected from the list by comparing the sum of integers from the start and end of the list with the ceiling and floor of k/2, respectively. The function returns this maximum number of integers.

