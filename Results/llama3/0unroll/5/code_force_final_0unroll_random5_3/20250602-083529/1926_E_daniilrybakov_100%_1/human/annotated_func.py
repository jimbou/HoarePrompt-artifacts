#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5 * 10^4) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^9).
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        s = 0
        
        m = 1
        
        while n:
            x = (n + 1) // 2
            n //= 2
            if s < k and k <= s + x:
                break
            s += x
            m *= 2
        
        print((2 * (k - s) - 1) * m)
        
    #State: The output will be t lines, each containing a single integer. The integer on each line will be the result of the calculation (2 * (k - s) - 1) * m for the corresponding input values of n and k.

#Overall this is what the function does:This function reads a series of input pairs (n, k) from standard input, where n and k are integers, and for each pair, it calculates and prints a single integer result based on a specific formula involving n and k. The function processes multiple input pairs, as specified by an initial integer t, and outputs the corresponding results, one per line.

