#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of an integer n (2 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: The output state will contain `t` lines, each containing the difference between the maximum and minimum numbers in the corresponding test case. The value of `t` remains unchanged.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and outputs the difference between the maximum and minimum numbers in each test case. It accepts no parameters and returns no value, instead printing the results directly. The function's purpose is to calculate and display the differences between the maximum and minimum values in a series of test cases, with the number of test cases and the values within each case provided as input.

