#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t, then t pairs of integers (n, k) such that 1 <= t <= 5 * 10^4, 1 <= k <= n <= 10^9.
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        L = []
        
        while n:
            m = (n + 1) // 2
            n -= m
        
        tot = 0
        
        pow = 1
        
        for a in L:
            if tot < k and k <= tot + a:
                print(pow * (2 * k - 1))
                break
            tot += a
            k -= tot
            pow *= 2
        
    #State: The output state will contain t lines, each containing a single integer. The integer on each line will be the result of the calculation pow * (2 * k - 1) for the corresponding input pair (n, k). The values of t, n, and k will remain unchanged.

#Overall this is what the function does:This function reads input from stdin, processes t pairs of integers (n, k), and prints t lines of output, each containing a single integer calculated as pow * (2 * k - 1) for the corresponding input pair (n, k). The function does not modify the input values of t, n, and k.

