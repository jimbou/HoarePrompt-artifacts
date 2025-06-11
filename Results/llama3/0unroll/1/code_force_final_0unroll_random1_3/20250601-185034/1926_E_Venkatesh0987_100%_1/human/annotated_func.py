#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 <= t <= 5 * 10^4), and each of the remaining t inputs is a pair of integers n and k (1 <= k <= n <= 10^9).
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
        
    #State: The output state is a list of t integers, each representing the result of the calculation for the corresponding input pair (n, k). The calculation is based on the given formula, which depends on whether k is greater than (n + 1) // 2 or not. If k is greater, the calculation involves a series of while loops that update variables s, d, i, g, h, and p, ultimately leading to the calculation of y. If k is not greater, the calculation is simply 2 * k - 1.

#Overall this is what the function does:Calculates and prints a list of integers based on input pairs of integers (n, k), where each integer in the output list represents the result of a calculation that depends on whether k is greater than (n + 1) // 2 or not. If k is greater, the calculation involves a series of iterative updates to variables, ultimately leading to the calculation of a value y. If k is not greater, the calculation is simply 2 * k - 1. The function processes multiple input pairs and prints the corresponding results.

