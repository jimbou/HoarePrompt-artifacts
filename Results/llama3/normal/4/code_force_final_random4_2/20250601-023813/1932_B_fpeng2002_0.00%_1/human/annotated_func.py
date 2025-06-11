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
        
    #State: num_tests is 0, n is an integer between 1 and 100 inclusive, nums is a list of n integers between 1 and 10^6 inclusive, start_year is (((((0 + 1) // nums[0] + 1) * nums[0] + 1 // nums[1] + 1) * nums[1] + 1) // nums[2] + 1) * nums[2], x is n - 1, stdin contains no test cases, and the start_year is printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then calculates a "start year" based on these integers, printing the result for each test case. The function continues this process until all test cases have been read from standard input, at which point it terminates.

