#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5 * 10^4) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^9).
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
        
    #State: The output state will be a list of `t` integers, each representing the result of the calculation `(2 * (k - (s - n)) - 1) * m` for the corresponding input values of `n` and `k`. The values of `t`, `n`, and `k` will remain unchanged.

#Overall this is what the function does:Calculates and prints a list of integers based on input values of `t`, `n`, and `k`, where each integer represents the result of a specific calculation involving `n` and `k`, without modifying the input values.

