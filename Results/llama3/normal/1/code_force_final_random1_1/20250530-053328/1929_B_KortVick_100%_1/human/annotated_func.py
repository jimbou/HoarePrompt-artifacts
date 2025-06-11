#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 1000). Each of the following t lines contains two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2).
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: `t` is an integer equal to 0, `n` and `k` are reassigned to the values from the last line of input, stdin is empty, `_` exists. If `4 * n - 2` equals `k`, the value of `k // 2 + 1` which is an integer between 1 and 2 * 10^8 (inclusive) is being printed. Otherwise, the ceiling of `k` divided by 2 is being printed.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains an integer t, and each subsequent line contains two integers n and k. It then iterates t times, processing each pair of n and k values. If 4n-2 equals k, it prints k//2 + 1; otherwise, it prints the ceiling of k divided by 2. After processing all input lines, the function leaves stdin empty and reassigns n and k to the values from the last line of input.

