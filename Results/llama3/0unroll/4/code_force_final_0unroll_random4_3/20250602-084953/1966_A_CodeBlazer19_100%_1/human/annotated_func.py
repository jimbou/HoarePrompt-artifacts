#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 100, 2 <= k <= 100). The second line contains n integers c_1, c_2, ..., c_n (1 <= c_i <= 100).
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = [l.count(j) for j in set(l)]
        
        if max(p) >= k:
            print(k - 1)
        else:
            print(n)
        
    #State: The output state is a list of t integers, where each integer is either k-1 or n, depending on whether the maximum count of any integer in the list is greater than or equal to k. The value of t remains unchanged, and the input state is consumed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of a list of integers and a target count. It then determines the maximum count of any integer in the list and prints either the target count minus one or the total number of integers in the list, depending on whether the maximum count is greater than or equal to the target count. The function processes all test cases and produces a list of output values, one for each test case.

