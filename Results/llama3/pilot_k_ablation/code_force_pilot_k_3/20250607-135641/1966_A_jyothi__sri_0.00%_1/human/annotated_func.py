#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 100, 2 <= k <= 100). The second line contains n integers c_1, c_2, ..., c_n (1 <= c_i <= 100).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        h = {}
        
        ans = n
        
        for i in a:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
            if h[i] >= k:
                ams = k - 1
        
        print(ans)
        
    #State: `n` is an integer, `k` is an integer, `a` is an empty list, `h` is a dictionary where each key is an integer from the original list `a` and its corresponding value is the count of that integer in the original list `a`, `ans` is equal to `k-1` if any count in `h` is greater than or equal to `k`, otherwise `ans` is equal to `n`, `_` is equal to `t`, stdin is empty, and the value of `ans` which is either `k-1` if any count in `h` is greater than or equal to `k`, otherwise `n` is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two lines: the first line contains two integers n and k, and the second line contains n integers. It then counts the occurrences of each integer in the second line and determines the minimum number of operations required to make all counts less than k. If any count is greater than or equal to k, the minimum number of operations is k-1; otherwise, it is n. The function prints the minimum number of operations for each test case.

