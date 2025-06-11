#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers n and k (1 <= n <= 100, 0 <= k <= n*(n-1)/2).
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: `t` is an integer between 1 and 10^3, `i` is `t`, `n` and `k` are integers that were inputted from stdin which is now empty. If `k` is greater than or equal to `n - 1`, the number 1 is being printed. Otherwise, the value of `n` which is an integer that was inputted from stdin is being printed, and either the number 1 or the value of `n` is being printed, depending on the else part.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each case consists of two integers, n and k. It then prints the minimum number of operations required to make all pairs of elements in a set of n elements connected, given that k connections already exist. If k is greater than or equal to n-1, it prints 1, indicating that all elements are already connected. Otherwise, it prints n, indicating that n-1 connections are needed to connect all elements. The function processes all test cases and prints the result for each case.

