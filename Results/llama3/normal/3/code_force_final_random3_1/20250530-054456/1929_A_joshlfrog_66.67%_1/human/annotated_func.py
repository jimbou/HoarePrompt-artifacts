#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 500) followed by t test cases. Each test case consists of an integer n (2 ≤ n ≤ 100) followed by n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 10^9).
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
        
    #State: t is at least 1, e is t-1, stdin is empty, l is an integer between 2 and 100, nums is a list of l integers between 1 and 10^9, i is l-1, x is the maximum value in nums, y is the minimum value in nums, and the difference between the maximum and minimum values in the list nums which is x - y is being printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a list of integers. For each test case, it finds the maximum and minimum values in the list and prints their difference. The function processes multiple test cases, as specified by the initial input, and does not return any value.

