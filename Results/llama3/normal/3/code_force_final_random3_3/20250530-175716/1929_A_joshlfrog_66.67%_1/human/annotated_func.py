#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the number of elements in the array) and then a list of integers. The integers in the list are between 1 and 10^9 (inclusive).
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
        
    #State: t is a positive integer, e is equal to t, l is an integer, nums is a list of integers between 1 and 10^9 (inclusive), i is equal to l, x is the maximum value in nums, and y is the minimum value in nums, and the difference between the maximum and minimum values in the list nums is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (the number of elements in the array) followed by a list of integers. It then finds the maximum and minimum values in each list and prints their difference. The function processes all test cases and outputs the differences for each case.

