#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line is an integer n (2 <= n <= 100). The second line is a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    t = int(input())
    for e in range(t):
        l = int(input())
        
        nums = [int(x) for x in input().split()]
        
        x = 0
        
        y = 100000000
        
        for i in range(l):
            if nums[i] > x:
                x = nums[i]
            if nums[i] < y:
                y = nums[i]
        
        print(x - y)
        
    #State: t is an integer between 2 and 100 (inclusive), e is t-1, l is an integer, nums is a list of integers, x is the maximum value in nums, y is the minimum value in nums, i is l-1, and stdin contains no test cases, and the difference between the maximum value and the minimum value in the list nums is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then finds the maximum and minimum values in each list and prints their difference. The function processes all test cases and does not return any value, instead, it prints the results directly to the console.

