#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^3). Each of the following t lines contains two integers n and k (1 <= n <= 100, 0 <= k <= n*(n-1)/2).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: `_` is t-1, `n` is an integer, `k` is an integer, stdin is empty, and this is printed: the value of `n` if `n` is less than or equal to `k+1`, otherwise 1

#Overall this is what the function does:Reads a series of input lines from stdin, where the first line contains the number of test cases (t), and each subsequent line contains two integers (n and k). For each test case, it prints the value of n if n is less than or equal to k+1, otherwise it prints 1. After processing all test cases, stdin is empty.

