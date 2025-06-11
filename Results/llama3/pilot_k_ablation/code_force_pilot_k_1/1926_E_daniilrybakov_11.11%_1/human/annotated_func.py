#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 50000) and then t pairs of integers n and k (1 <= k <= n <= 10^9).
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
        
    #State: t is 0, stdin is empty, n_back, s, n, m, and k are undefined (or have arbitrary values), and the loop has printed t lines of output.

#Overall this is what the function does:The function reads a series of input pairs from stdin, where each pair consists of two integers, n and k. It then calculates and prints a value for each pair, based on a series of mathematical operations involving n and k. The function continues this process until all input pairs have been processed, at which point stdin is empty and the function has printed a corresponding number of output lines.

