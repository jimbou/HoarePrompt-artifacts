#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6).
    num_tests = int(input())
    while num_tests > 0:
        num_tests -= 1
        
        n = int(input())
        
        nums = [int(x) for x in input().split(' ')]
        
        start_year = 0
        
        for x in range(0, len(nums)):
            start_year = ((start_year + 1) // nums[x] + 1) * nums[x]
        
        print(start_year)
        
    #State: num_tests = 0, start_year = the last calculated start_year value

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then calculates a "start year" value for each test case by iteratively updating a running total based on the given integers. The calculated start year value for each test case is printed to standard output. The function continues processing test cases until all input has been consumed.

