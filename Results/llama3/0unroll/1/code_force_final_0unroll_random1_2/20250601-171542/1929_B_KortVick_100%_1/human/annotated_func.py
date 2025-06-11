#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 1000). Each of the following t lines contains two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2).
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: The output state will contain `t` lines of output, each containing an integer. For each line, if `k` is equal to `4n - 2`, the output will be `k // 2 + 1`, otherwise the output will be `ceil(k / 2)`. The value of `t` remains unchanged.

#Overall this is what the function does:This function reads a series of input lines from standard input, where the first line contains an integer t representing the number of test cases, and each subsequent line contains two integers n and k. It then calculates and prints the ceiling of k divided by 2 for each test case, except when k is equal to 4n - 2, in which case it prints k divided by 2 plus 1. The function produces t lines of output, each containing a single integer, and leaves the input variable t unchanged.

