#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 500) followed by t test cases. Each test case consists of an integer n (2 ≤ n ≤ 100) followed by n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 10^9).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: t is 0, n is an integer between 2 and 100 inclusive, nums is a sorted list of n integers in descending order, _ is t-1, stdin contains 0 test cases, and the sum of the first two elements of the list nums which are the two largest numbers in the list is being printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It sorts the integers in descending order and prints the sum of the two largest numbers in each test case. The function processes all test cases and then terminates, leaving the input stream empty.

