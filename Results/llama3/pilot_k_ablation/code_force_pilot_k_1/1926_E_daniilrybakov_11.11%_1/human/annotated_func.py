#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 5 * 10^4). Each of the following t lines contains two integers n and k (1 <= k <= n <= 10^9).
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        n_back = n
        
        s = (n + 1) // 2
        
        n = (n + 1) // 2
        
        m = 1
        
        while s < k:
            if n == 0:
                s = n_back
                n = 1
                break
            m *= 2
            n //= 2
            s += n
        
        print((2 * (k - (s - n)) - 1) * m)
        
    #State: `t` is an integer between 0 and 5 * 10^4 (inclusive), `n_back` is an integer between 1 and 10^9 (inclusive), `s` is equal to `k`, `n` is an integer between 1 and 5 * 10^8 (inclusive) divided by 2 to the power of the number of times the loop executed, `m` is 2 to the power of the number of times the loop executed, stdin is empty.

#Overall this is what the function does:The function reads multiple lines of input from stdin, where the first line contains an integer t (1 <= t <= 5 * 10^4) and each of the following t lines contains two integers n and k (1 <= k <= n <= 10^9). It then performs calculations based on these inputs and prints the results. The function iteratively updates the values of n, s, and m until s is equal to k, and then prints the calculated result. The function does not modify the input variables and leaves stdin empty after execution.

