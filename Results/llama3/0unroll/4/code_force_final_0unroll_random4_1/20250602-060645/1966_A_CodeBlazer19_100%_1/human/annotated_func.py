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
        
    #State: The output state will be a list of integers, where each integer is either `k - 1` or `n`, depending on whether the maximum count of any integer in the list `l` is greater than or equal to `k`. The length of the output list will be equal to `t`, the number of test cases.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the results. For each test case, it reads two integers (n and k) and a list of n integers, then determines the maximum count of any integer in the list. If the maximum count is greater than or equal to k, it prints k - 1; otherwise, it prints n. The function repeats this process for a specified number of test cases (t) and outputs a list of results, one for each test case.

