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
        
    #State: The output will be the difference between the maximum and minimum values in each test case, printed t times.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a list of integers. It then calculates and prints the difference between the maximum and minimum values in each list, repeating this process for the specified number of test cases.

