#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 5 * 10^4), then t pairs of integers n and k (1 <= k <= n <= 10^9).
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        L = []
        
        while n:
            m = (n + 1) // 2
            n -= m
            L.append(m)
        
        tot = 0
        
        pow = 1
        
        for a in L:
            if tot < k and k <= tot + a:
                print(pow * (2 * (k - tot) - 1))
            tot += a
            pow *= 2
        
    #State: The loop will print t lines, each containing an integer. The integer on each line will be the value of the expression `pow * (2 * (k - tot) - 1)` for the corresponding pair of integers n and k from the input. The value of `pow` will be a power of 2, and the value of `k - tot` will be a non-negative integer less than the value of `a` in the inner loop.

#Overall this is what the function does:This function reads input from stdin, processes t pairs of integers n and k, and prints t lines, each containing an integer calculated based on the values of n and k. For each pair, it calculates a value using the expression `pow * (2 * (k - tot) - 1)`, where `pow` is a power of 2 and `k - tot` is a non-negative integer less than the value of `a` in the inner loop. The function does not return any value, but instead prints the calculated integers to the console.

