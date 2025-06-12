#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 1000). Each of the following t lines contains two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2).
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if k % 2 == 0 and k // 2 % 2 == 1:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: `t` is an integer between 0 and 1000 (inclusive), `_` is equal to `t`, `n` is an integer between 2 and 10^8 (inclusive), `k` is an integer between 1 and 4n - 2 (inclusive), stdin is empty.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers, n and k. It then calculates and prints the ceiling of k/2 for each test case, with a special case for when k is even and k/2 is odd, in which case it prints k/2 + 1. The function processes all test cases and leaves the standard input empty.

