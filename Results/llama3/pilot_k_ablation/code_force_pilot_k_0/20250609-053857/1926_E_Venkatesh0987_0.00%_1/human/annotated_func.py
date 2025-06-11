#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 <= t <= 5 * 10^4), and each of the next t inputs is a pair of space-separated integers n and k (1 <= k <= n <= 10^9).
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
        
    #State: The output state will be a list of t integers, each representing the result of the calculation for the corresponding input pair (n, k). The calculation is based on the conditions and formulas specified in the loop body. If k is greater than (n + 1) // 2, the calculation involves a series of while loops and bit manipulation, resulting in a value y. If k is less than or equal to (n + 1) // 2, the calculation simply results in 2 * k - 1. The output state will contain the results of these calculations for each input pair.

#Overall this is what the function does:Calculates and prints the result of a mathematical operation for each input pair (n, k), where the operation depends on whether k is greater than (n + 1) // 2. If true, the result is calculated through a series of while loops and bit manipulation, otherwise, the result is simply 2 * k - 1. The function processes multiple input pairs and prints the corresponding results.

