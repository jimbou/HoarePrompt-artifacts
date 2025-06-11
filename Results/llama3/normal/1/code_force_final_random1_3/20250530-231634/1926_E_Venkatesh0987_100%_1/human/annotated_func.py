#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 50000) and then t pairs of integers n and k (1 <= k <= n <= 10^9).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        s = 0
        
        i = 0
        
        d = n
        
        h = n
        
        p = 1
        
        g = 0
        
        if k > (n + 1) // 2:
            while s < k and d > 0:
                s += (d + 1) // 2
                d -= (d + 1) // 2
                i += 1
            while p <= i - 1:
                g += (h + 1) // 2
                h -= (h + 1) // 2
                p += 1
            f = k - g
            y = 2 ** (i - 1) * (2 * f - 1)
            print(y)
        else:
            print(2 * k - 1)
        
    #State: _ is t, s is either k or 0, i is either the smallest integer i such that s >= k or 0, d is either 0 or n, h is either 0 or n, p is either i or 1, g is either n or the sum of (n + 1) // 2^j for j from 1 to i - 1, f is k - g, and y is either 2^(i-1) * (2k - 2n - 1) or 2k - 1 depending on whether k is greater than (n + 1) // 2 or not.

#Overall this is what the function does:This function reads a series of input pairs (n, k) from standard input, where n and k are integers, and for each pair, it calculates and prints a value based on whether k is greater than (n + 1) // 2. If k is greater, it calculates the value using a series of iterations and bit manipulations, otherwise, it simply prints 2 * k - 1. The function processes multiple input pairs as specified by an initial integer t, which indicates the number of pairs to follow.

