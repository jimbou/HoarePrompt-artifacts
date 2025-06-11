#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6).
    num_tests = int(input())
    while num_tests > 0:
        num_tests -= 1
        
        n = int(input())
        
        nums = [int(x) for x in input().split(' ')]
        
        start_year = 0
        
        for x in range(0, len(nums)):
            start_year = ((start_year + 1) // nums[x] + 1) * nums[x]
        
        print(start_year)
        
    #State: num_tests is 0, n is an integer between 1 and 100, nums is a list of n integers between 1 and 10^6, start_year is the result of the loop body executed n times with the initial value of start_year being 0, stdin is empty, and x is n-1.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then calculates the start year for each test case by iteratively updating the start year based on the given integers, and prints the final start year for each test case. The function continues this process until all test cases have been processed, at which point the standard input is empty.

