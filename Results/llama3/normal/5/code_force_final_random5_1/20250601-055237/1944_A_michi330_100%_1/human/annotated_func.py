#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^3) — the number of test cases. Each of the following t lines contains two integers n and k (1 <= n <= 100, 0 <= k <= n * (n - 1) / 2).
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: `t` is an integer between 1 and 10^3 (inclusive), `i` is `t`, `n` and `k` are integers that were previously in stdin and are now assigned to `n` and `k` respectively, `stdin` contains 0 lines of input. If `k` is greater than or equal to `n - 1`, then 1 is printed. Otherwise, the value of `n` is printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers, n and k. It then prints the minimum number of operations required to make all pairs of elements in a set of n elements connected, given that k connections already exist. If k is greater than or equal to n-1, it prints 1, indicating that all elements are already connected. Otherwise, it prints n, indicating that all elements need to be connected. The function processes all test cases and prints the result for each case.

