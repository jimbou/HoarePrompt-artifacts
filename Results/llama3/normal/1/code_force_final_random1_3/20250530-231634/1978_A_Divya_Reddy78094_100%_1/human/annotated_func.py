#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 500) followed by t test cases. Each test case consists of an integer n (2 ≤ n ≤ 100) followed by n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 10^9).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: t is 0, _ is t, n is an integer, nums is a list of integers, stdin is empty, and the sum of the maximum of all elements in the list nums except the last one and the last element of the list nums has been printed t times.

#Overall this is what the function does:Reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. For each test case, it prints the sum of the maximum of all elements except the last one and the last element. The function processes all test cases and leaves the standard input empty.

