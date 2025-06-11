#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 5 * 10^4) and then t pairs of integers n and k (1 <= k <= n <= 10^9).
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
            y = 2 ** (i - 1) * f
            print(y)
        else:
            print(2 * k - 1)
        
    #State: t pairs of integers have been processed, and the corresponding output values have been printed. The loop variables _ is equal to t, n and k are the last pair of integers from stdin, s, i, d, h, p, g are integers, and the output values are either 2 * k - 1 or 2^(i-1) * (k - g) depending on whether k is less than or equal to (n + 1) // 2 or greater than (n + 1) // 2, respectively.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, where each pair consists of a number n and a number k. For each pair, it calculates and prints a value based on whether k is less than or equal to half of n plus one. If k is less than or equal to half of n plus one, it prints 2 times k minus 1. Otherwise, it calculates a more complex value involving powers of 2 and prints that. The function processes all input pairs and prints the corresponding output values.

