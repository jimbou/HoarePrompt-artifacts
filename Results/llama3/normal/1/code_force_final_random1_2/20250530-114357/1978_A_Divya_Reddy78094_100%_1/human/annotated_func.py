#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case contains an integer n (2 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: t is an integer (1 <= t <= 500), stdin contains 0 test cases, n is an integer (2 <= n <= 100), nums is a list of n integers (1 <= a_i <= 10^9), and the sum of the maximum of all elements in the list except the last one and the last element in the list is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then calculates and prints the sum of the maximum of all elements in the list except the last one and the last element in the list, for each test case. The function processes multiple test cases, as specified by the initial integer t, and does not return any value.

